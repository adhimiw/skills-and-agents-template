# Hostinger SSH notes (shared hosting)

- Plan must be Premium or higher for SSH. Scope is home-dir jailed (`~` and below).
- Enable in hPanel: Websites > Dashboard > SSH Access > Enable, note hostname/user/port.
- This skill defaults to `u244089748 @ 145.79.210.59 : 65002`.
- Key auth: generate `~/.ssh/hostinger_u244089748_ed25519`, paste `.pub` into hPanel > SSH Access > Add SSH Key, then `hssh.py exec "pwd && whoami"`.
- Shared-hosting quirks: no root, no custom ports listening, `php -v` / `ls ~/domains` useful probes.
- Never store the account password. If it was ever pasted in chat/logs, change it in hPanel > SSH Access > Change password, then re-add keys.
