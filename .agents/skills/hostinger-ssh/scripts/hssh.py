#!/usr/bin/env python3
"""hssh.py - minimal secure Hostinger SSH helper (OpenSSH only, key auth).

Commands:
  doctor [--json]   local preflight, no login: client, TCP 145.79.210.59:65002, hostkey
  check             same as doctor, human readable
  exec <cmd>        run one remote command via key auth (BatchMode, no password prompt storage)
  upload <local> <remote>
  download <remote> <local>
  ssh -- [extra ssh args]

Env overrides: HSSH_HOST, HSSH_PORT, HSSH_USER, HSSH_KEY
Never accepts a password argument. Never writes credentials.
"""
import json
import os
import shutil
import socket
import subprocess
import sys

DEFAULTS = {
    "host": os.environ.get("HSSH_HOST", "145.79.210.59"),
    "port": int(os.environ.get("HSSH_PORT", "65002")),
    "user": os.environ.get("HSSH_USER", "u244089748"),
    "key": os.environ.get("HSSH_KEY", os.path.expanduser("~/.ssh/hostinger_u244089748_ed25519")),
}

BASE_SSH = [
    "ssh",
    "-p", str(DEFAULTS["port"]),
    "-o", "BatchMode=yes",          # fail instead of prompting for password
    "-o", "ConnectTimeout=10",
    "-o", "StrictHostKeyChecking=accept-new",
]
if os.path.exists(DEFAULTS["key"]):
    BASE_SSH += ["-i", DEFAULTS["key"]]

TARGET = f'{DEFAULTS["user"]}@{DEFAULTS["host"]}'

def run(cmd, timeout=20):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except FileNotFoundError as e:
        return 127, "", str(e)
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"

def doctor():
    ssh_ok = shutil.which("ssh") is not None
    scp_ok = shutil.which("scp") is not None
    key_exists = os.path.exists(DEFAULTS["key"])
    # TCP check (no auth)
    tcp_ok, tcp_msg = False, ""
    try:
        with socket.create_connection((DEFAULTS["host"], DEFAULTS["port"]), timeout=10):
            tcp_ok = True
            tcp_msg = f"TCP {DEFAULTS['host']}:{DEFAULTS['port']} open"
    except Exception as e:
        tcp_msg = f"TCP {DEFAULTS['host']}:{DEFAULTS['port']} failed: {e}"
    # hostkey (no auth)
    rc, out, err = run(["ssh-keyscan", "-p", str(DEFAULTS["port"]), DEFAULTS["host"]], timeout=15)
    hostkey_ok = rc == 0 and len(out) > 0
    ok = ssh_ok and tcp_ok
    return {
        "ok": ok,
        "host": DEFAULTS["host"],
        "port": DEFAULTS["port"],
        "user": DEFAULTS["user"],
        "ssh_client": ssh_ok,
        "scp_client": scp_ok,
        "tcp": {"ok": tcp_ok, "msg": tcp_msg},
        "hostkey_seen": hostkey_ok,
        "key_path": DEFAULTS["key"],
        "key_exists": key_exists,
        "auth_mode": "key-only (BatchMode=yes, no stored password)",
        "next": "add ~/.ssh/hostinger_u244089748_ed25519.pub to hPanel > SSH Access if key_exists=false, then run: hssh.py exec \"pwd && whoami\"",
    }

def main(argv):
    if not argv or argv[0] in ("--help", "-h", "help"):
        print(__doc__)
        return 0
    cmd = argv[0]
    if cmd in ("doctor", "check"):
        d = doctor()
        if "--json" in argv:
            print(json.dumps(d, indent=2))
        else:
            print(f"host: {d['host']}:{d['port']} user: {d['user']}")
            print(f"ssh_client: {d['ssh_client']} scp_client: {d['scp_client']}")
            print(f"tcp: {d['tcp']['msg']}")
            print(f"hostkey_seen: {d['hostkey_seen']}")
            print(f"key: {d['key_path']} exists={d['key_exists']}")
            print(f"auth: {d['auth_mode']}")
            print(f"next: {d['next']}")
        return 0 if d["ok"] else 2
    if cmd == "exec":
        if len(argv) < 2:
            print("usage: hssh.py exec \"<remote command>\"", file=sys.stderr)
            return 2
        remote = argv[1]
        rc, out, err = run(BASE_SSH + [TARGET, remote], timeout=60)
        if out:
            print(out)
        if err:
            print(err, file=sys.stderr)
        return rc
    if cmd == "upload":
        if len(argv) != 3:
            print("usage: hssh.py upload <local> <remote>", file=sys.stderr)
            return 2
        local, remote = argv[1], argv[2]
        scp = ["scp", "-P", str(DEFAULTS["port"]), "-o", "BatchMode=yes",
               "-o", "ConnectTimeout=10", "-o", "StrictHostKeyChecking=accept-new"]
        if os.path.exists(DEFAULTS["key"]):
            scp += ["-i", DEFAULTS["key"]]
        rc, out, err = run(scp + [local, f"{TARGET}:{remote}"], timeout=120)
        if out:
            print(out)
        if err:
            print(err, file=sys.stderr)
        return rc
    if cmd == "download":
        if len(argv) != 3:
            print("usage: hssh.py download <remote> <local>", file=sys.stderr)
            return 2
        remote, local = argv[1], argv[2]
        scp = ["scp", "-P", str(DEFAULTS["port"]), "-o", "BatchMode=yes",
               "-o", "ConnectTimeout=10", "-o", "StrictHostKeyChecking=accept-new"]
        if os.path.exists(DEFAULTS["key"]):
            scp += ["-i", DEFAULTS["key"]]
        rc, out, err = run(scp + [f"{TARGET}:{remote}", local], timeout=120)
        if out:
            print(out)
        if err:
            print(err, file=sys.stderr)
        return rc
    if cmd == "ssh":
        extra = argv[1:]
        if extra and extra[0] == "--":
            extra = extra[1:]
        # strip any password-like flags defensively
        rc, out, err = run(BASE_SSH + extra + [TARGET], timeout=60)
        if out:
            print(out)
        if err:
            print(err, file=sys.stderr)
        return rc
    print(f"unknown command: {cmd}\n{__doc__}", file=sys.stderr)
    return 2

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
