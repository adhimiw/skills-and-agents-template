#!/usr/bin/env python3
"""
ichome_ssh.py - Autonomous SSH connector for ICHOME server (IC200@3.6).
Provides auto-routing (LAN first, Tailscale fallback), remote execution,
file push/pull, and health telemetry for AI agents.
"""

import sys
import os
import socket
import subprocess
import argparse
import json
from pathlib import Path

# Configuration defaults
DEFAULT_USER = os.getenv("ICHOME_USER", "adhithan")
LAN_HOSTS = [os.getenv("ICHOME_LAN_HOST", "192.168.1.5"), "192.168.1.4"]
TAILSCALE_HOST = os.getenv("ICHOME_TS_HOST", "100.111.215.107")
DEFAULT_PORT = int(os.getenv("ICHOME_PORT", "22"))
DEFAULT_KEY = os.getenv("ICHOME_KEY", str(Path.home() / ".ssh" / "id_ed25519"))
SSH_TIMEOUT = int(os.getenv("ICHOME_TIMEOUT", "6"))
ICHOME_MAC = "00:e0:4c:f4:97:f6"


def find_ip_by_mac(mac: str) -> str:
    """Find IP matching MAC address from local ARP/neighbor table."""
    try:
        out = subprocess.run(["ip", "neigh"], capture_output=True, text=True, timeout=2)
        for line in out.stdout.splitlines():
            if mac.lower() in line.lower():
                parts = line.split()
                if parts:
                    return parts[0]
    except Exception:
        pass
    return ""


def check_tcp_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Test whether a remote TCP port is accepting connections."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def resolve_active_host() -> str:
    """Auto-detect whether to route via dynamic LAN IP or Tailscale."""
    manual_host = os.getenv("ICHOME_HOST")
    if manual_host:
        return manual_host

    # Try ARP lookup by hardware MAC
    arp_ip = find_ip_by_mac(ICHOME_MAC)
    if arp_ip and check_tcp_port(arp_ip, DEFAULT_PORT, timeout=0.8):
        return arp_ip

    # Try candidate LAN IPs
    for host in LAN_HOSTS:
        if check_tcp_port(host, DEFAULT_PORT, timeout=0.8):
            return host

    if check_tcp_port(TAILSCALE_HOST, DEFAULT_PORT, timeout=2.0):
        return TAILSCALE_HOST

    return "192.168.1.5"


def build_ssh_base_command(host: str, key_path: str = DEFAULT_KEY, user: str = DEFAULT_USER) -> list:
    cmd = [
        "ssh",
        "-o", "BatchMode=yes",
        "-o", "StrictHostKeyChecking=accept-new",
        "-o", f"ConnectTimeout={SSH_TIMEOUT}",
    ]
    if os.path.exists(key_path):
        cmd.extend(["-i", key_path])
    cmd.append(f"{user}@{host}")
    return cmd


def cmd_doctor(args):
    active_host = resolve_active_host()
    lan_ok = check_tcp_port(active_host, DEFAULT_PORT, 1.0)
    ts_ok = check_tcp_port(TAILSCALE_HOST, DEFAULT_PORT, 2.0)
    key_exists = os.path.exists(DEFAULT_KEY)

    info = {
        "server_name": "ichome",
        "node_alias": "IC200@3.6",
        "lan_host": active_host,
        "lan_ssh_open": lan_ok,
        "tailscale_host": TAILSCALE_HOST,
        "tailscale_ssh_open": ts_ok,
        "ssh_key_path": DEFAULT_KEY,
        "ssh_key_present": key_exists,
        "active_routed_host": active_host,
        "auth_user": DEFAULT_USER,
    }

    if getattr(args, "json", False):
        print(json.dumps(info, indent=2))
        return 0

    print("=== ICHOME SSH Connectivity Doctor ===")
    print(f"Server Alias       : {info['node_alias']} (ichome)")
    print(f"LAN Route          : {active_host}:{DEFAULT_PORT} -> {'ONLINE (Preferred)' if lan_ok else 'UNREACHABLE'}")
    print(f"Tailscale Route    : {TAILSCALE_HOST}:{DEFAULT_PORT} -> {'ONLINE' if ts_ok else 'OFFLINE/LOCAL'}")
    print(f"SSH Key            : {DEFAULT_KEY} [{'FOUND' if key_exists else 'MISSING'}]")
    print(f"Active Selected Host: {active_host}")
    print("=======================================")
    return 0 if (lan_ok or ts_ok) and key_exists else 1


def cmd_exec(args):
    host = resolve_active_host()
    ssh_cmd = build_ssh_base_command(host)
    remote_cmd = " ".join(args.command)
    ssh_cmd.append(remote_cmd)

    proc = subprocess.run(ssh_cmd)
    return proc.returncode


def cmd_status(args):
    host = resolve_active_host()
    remote_script = (
        "echo '=== HARDWARE TELEMETRY ===' && "
        "uptime && "
        "free -m && "
        "df -h / /home 2>/dev/null | awk '!seen[$1]++' && "
        "echo '=== CONTAINER STATUS ===' && "
        "docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' && "
        "echo '=== SYSTEMD CORE SERVICES ===' && "
        "systemctl is-active ichome-portal.service hermes-nano.service"
    )
    ssh_cmd = build_ssh_base_command(host)
    ssh_cmd.append(remote_script)
    proc = subprocess.run(ssh_cmd)
    return proc.returncode


def cmd_push(args):
    host = resolve_active_host()
    local_path = os.path.abspath(args.local)
    remote_dest = f"{DEFAULT_USER}@{host}:{args.remote}"

    # Use rsync if available, fallback to scp
    rsync_bin = subprocess.run(["which", "rsync"], capture_output=True, text=True)
    if rsync_bin.returncode == 0:
        cmd = ["rsync", "-avz", "--progress"]
        if os.path.exists(DEFAULT_KEY):
            cmd.extend(["-e", f"ssh -i {DEFAULT_KEY} -o BatchMode=yes -o StrictHostKeyChecking=accept-new"])
        cmd.extend([local_path, remote_dest])
    else:
        cmd = ["scp", "-r", "-o", "BatchMode=yes"]
        if os.path.exists(DEFAULT_KEY):
            cmd.extend(["-i", DEFAULT_KEY])
        cmd.extend([local_path, remote_dest])

    proc = subprocess.run(cmd)
    return proc.returncode


def cmd_pull(args):
    host = resolve_active_host()
    local_path = os.path.abspath(args.local)
    remote_src = f"{DEFAULT_USER}@{host}:{args.remote}"

    rsync_bin = subprocess.run(["which", "rsync"], capture_output=True, text=True)
    if rsync_bin.returncode == 0:
        cmd = ["rsync", "-avz", "--progress"]
        if os.path.exists(DEFAULT_KEY):
            cmd.extend(["-e", f"ssh -i {DEFAULT_KEY} -o BatchMode=yes -o StrictHostKeyChecking=accept-new"])
        cmd.extend([remote_src, local_path])
    else:
        cmd = ["scp", "-r", "-o", "BatchMode=yes"]
        if os.path.exists(DEFAULT_KEY):
            cmd.extend(["-i", DEFAULT_KEY])
        cmd.extend([remote_src, local_path])

    proc = subprocess.run(cmd)
    return proc.returncode


def main():
    parser = argparse.ArgumentParser(
        description="ICHOME SSH - Agent control bridge for home server IC200@3.6"
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # doctor
    p_doctor = subparsers.add_parser("doctor", help="Inspect network and SSH health")
    p_doctor.add_argument("--json", action="store_true", help="Output diagnostic in JSON")
    p_doctor.set_defaults(func=cmd_doctor)

    # exec
    p_exec = subparsers.add_parser("exec", help="Execute remote command on ichome")
    p_exec.add_argument("command", nargs=argparse.REMAINDER, help="Command to run")
    p_exec.set_defaults(func=cmd_exec)

    # status
    p_status = subparsers.add_parser("status", help="Get hardware & service telemetry")
    p_status.set_defaults(func=cmd_status)

    # push
    p_push = subparsers.add_parser("push", help="Push file or folder to ichome")
    p_push.add_argument("local", help="Local source path")
    p_push.add_argument("remote", help="Remote destination path")
    p_push.set_defaults(func=cmd_push)

    # pull
    p_pull = subparsers.add_parser("pull", help="Pull file or folder from ichome")
    p_pull.add_argument("remote", help="Remote source path")
    p_pull.add_argument("local", help="Local destination path")
    p_pull.set_defaults(func=cmd_pull)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
