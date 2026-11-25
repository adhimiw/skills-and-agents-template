---
name: hostinger-ssh
description: SSH into Hostinger shared hosting (u244089748 on 145.79.210.59:65002) via OpenSSH with key auth. Exec remote commands, upload/download via scp. Never stores passwords.
license: MIT
allowed-tools: Bash, Read
metadata:
  version: "1.0.0"
  host: "145.79.210.59"
  port: "65002"
  user: "u244089748"
  auth: "key-only, no-stored-password"
---

# /hostinger-ssh

Secure personal skill for your Hostinger shared-hosting SSH. Key-auth only. No password is ever written to disk by this skill.

## Connection defaults

- Host: `145.79.210.59`
- Port: `65002`
- User: `u244089748`
- Override per-run with env: `HSSH_HOST`, `HSSH_PORT`, `HSSH_USER`, `HSSH_KEY`

`SKILL_DIR` = directory containing this SKILL.md. Scripts live in `SKILL_DIR/scripts/`.

## First run — key setup (do this once)

Hostinger shared hosting supports SSH keys via hPanel > Websites > Dashboard > SSH Access > Add SSH Key. Password SSH works but is not used by this skill.

```bash
# 1. generate key if missing
ls ~/.ssh/hostinger_u244089748_ed25519 || ssh-keygen -t ed25519 -C "u244089748-hostinger" -f ~/.ssh/hostinger_u244089748_ed25519

# 2. show public key to paste into hPanel
cat ~/.ssh/hostinger_u244089748_ed25519.pub

# 3. after adding key in hPanel, test (key auth, no password on CLI)
python3 "${SKILL_DIR}/scripts/hssh.py" doctor --json
python3 "${SKILL_DIR}/scripts/hssh.py" check
```

## Usage

```bash
# preflight, no login (TCP + hostkey + client check)
python3 "${SKILL_DIR}/scripts/hssh.py" doctor --json

# run one remote command (key auth)
python3 "${SKILL_DIR}/scripts/hssh.py" exec "pwd && ls -la && php -v"

# upload / download (POSIX remote paths, home-dir jailed on shared hosting)
python3 "${SKILL_DIR}/scripts/hssh.py" upload ./local.zip ~/domains/example.com/public_html/app.zip
python3 "${SKILL_DIR}/scripts/hssh.py" download ~/error_log ./error_log

# raw ssh passthrough (extra ssh flags allowed after --)
python3 "${SKILL_DIR}/scripts/hssh.py" ssh -- -v -o BatchMode=yes
```

## Security rules

- NEVER put a password in `~/.ssh/config`, env files, skill files, or shell history.
- NEVER run with `sshpass -p <password>` or `SSH_ASKPASS` tricks. If key auth fails, prompt interactively, don't persist.
- Host key defaults to `accept-new`; a changed host key aborts.
- Remote scope on Premium shared hosting is home-dir jailed — don't assume root paths.
- All secrets stay in `~/.ssh/` (0600) or ssh-agent. This skill writes nothing credential-like.
