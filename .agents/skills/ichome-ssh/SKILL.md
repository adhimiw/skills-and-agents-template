---
name: ichome-ssh
description: Secure agent SSH bridge to the personal home server ICHOME (IC200@3.6). Provides auto-routing over LAN (192.168.1.4) or Tailscale WireGuard mesh (100.111.215.107), remote command execution, service telemetry, file synchronization, and container lifecycle management.
license: MIT
allowed-tools: Bash, Read
metadata:
  version: "1.0.0"
  lan_host: "192.168.1.4"
  tailscale_host: "100.111.215.107"
  user: "adhithan"
  port: 22
  auth: "ed25519-key-only"
  target_node: "IC200@3.6 (Debian 13)"
---

# /ichome-ssh

The authoritative SSH access and remote operations skill for all AI agents managing the **`ichome`** server (`IC200@3.6`).

This skill uses ed25519 key authentication with zero passwords stored on disk. It features automatic network routing: it automatically detects whether the agent is executing locally on the home LAN (`192.168.1.4:22`) or remotely across the Tailscale WireGuard mesh (`100.111.215.107:22`).

---

## Connection Endpoints & Defaults

| Environment | Host Address | Port | User | Auth Method |
| :--- | :--- | :--- | :--- | :--- |
| **Local Home LAN** | `192.168.1.4` | `22` | `adhithan` | `~/.ssh/id_ed25519` |
| **Tailscale Remote Mesh** | `100.111.215.107` | `22` | `adhithan` | `~/.ssh/id_ed25519` |

### Environment Overrides (Optional)
Agents may override connection parameters via environment variables:
* `ICHOME_HOST`: Force specific host IP or domain.
* `ICHOME_USER`: Override remote username (default: `adhithan`).
* `ICHOME_KEY`: Path to private SSH key (default: `~/.ssh/id_ed25519`).
* `ICHOME_TIMEOUT`: Connection timeout in seconds (default: `6`).

---

## Agent Usage & Commands

The skill script is located at:
`scripts/ichome_ssh.py`

### 1. Connection Doctor & Diagnostics
Check route availability, latency, and SSH key readiness:
```bash
python3 /home/adhithan/.agents/skills/ichome-ssh/scripts/ichome_ssh.py doctor
# Or output machine-readable JSON:
python3 /home/adhithan/.agents/skills/ichome-ssh/scripts/ichome_ssh.py doctor --json
```

### 2. Live Telemetry & Service Status
Fetch server uptime, CPU load, memory utilization, disk space, Docker containers, and systemd units in one step:
```bash
python3 /home/adhithan/.agents/skills/ichome-ssh/scripts/ichome_ssh.py status
```

### 3. Remote Command Execution
Run any bash command on `ichome`:
```bash
# General syntax
python3 /home/adhithan/.agents/skills/ichome-ssh/scripts/ichome_ssh.py exec "<command>"

# Examples
python3 /home/adhithan/.agents/skills/ichome-ssh/scripts/ichome_ssh.py exec "docker ps"
python3 /home/adhithan/.agents/skills/ichome-ssh/scripts/ichome_ssh.py exec "systemctl status ichome-portal.service"
python3 /home/adhithan/.agents/skills/ichome-ssh/scripts/ichome_ssh.py exec "ls -lh /home/adhithan/media/movies"
```

### 4. File Synchronization (Push & Pull)
Synchronize files and folders between the local workstation and `ichome`:
```bash
# Push local file or folder to server
python3 /home/adhithan/.agents/skills/ichome-ssh/scripts/ichome_ssh.py push ./local_script.py /home/adhithan/scripts/

# Pull file or folder from server
python3 /home/adhithan/.agents/skills/ichome-ssh/scripts/ichome_ssh.py pull /home/adhithan/logs/portal.log ./portal.log
```

---

## Server Service Inventory

| Service | Type | Port | Description |
| :--- | :--- | :--- | :--- |
| **ichome-portal** | Systemd Service | `5000` | All-in-One Tablet/Mobile Web Portal & CRUD Cloud |
| **hermes-nano** | Systemd Service | N/A | Telegram Bot (`@Ic2003_6bot`) powered by Mistral AI |
| **forgejo_git** | Docker Container | `3000`, `2222` | Self-hosted Git forge & agent skills repository |
| **jellyfin_media**| Docker Container | `8096` | Streaming cinema server |
| **navidrome_music**| Docker Container | `4533` | Subsonic-compatible music streamer |
| **stalwart_mail** | Docker Container | `8080`, `25`, `993` | All-in-one sovereign mail server |
| **tailscaled** | Systemd Service | N/A | WireGuard mesh tunnel daemon |

---

## Agent Operational Rules & Safety Guardrails

1. **Key Authentication Integrity:** Never attempt to pass plaintext passwords via SSH or modify `/etc/ssh/sshd_config` to enable password-based root login.
2. **Resource Preservation:** The host CPU is a dual-core Intel Core i3-2100 with 6GB RAM. Agents must avoid launching CPU-intensive unthrottled builds directly on the server without `nice -n 19`.
3. **Container Isolation:** Do not edit container mount volumes while containers are actively writing databases. Always perform graceful restarts via `docker restart <container>` or `docker stop <container>`.
4. **Permissions Enforcement:** The `amudhadevi` user home directory (`/home/amudhadevi`) must maintain mode `755` so that the portal service can read educational study materials.
