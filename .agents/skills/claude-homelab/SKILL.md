---
name: claude-homelab
description: Homelab orchestration and MCP server management based on jmagar/claude-homelab. Use when managing, querying, or troubleshooting homelab containers, Proxmox/VMs, Home Assistant, service healthchecks, network topology, and Tailscale mesh configurations.
allowed-tools: Read Write Edit Glob Grep
---

# Claude-Homelab: Homelab Orchestration & MCP Integration

## Overview

`claude-homelab` connects AI agents directly to self-hosted homelab environments, providing unified MCP (Model Context Protocol) tool calling, container diagnostics, infrastructure orchestration, and automated service recovery. Modeled after `jmagar/claude-homelab`, it enables agents to query service states, perform rolling restarts, inspect network meshes, and audit homelab metrics without manual SSH juggling.

---

## Triggers & Activation Scenarios

Activate this skill when:
- Querying the live status, ports, or logs of homelab services (Jellyfin, Forgejo, Navidrome, Stalwart).
- Troubleshooting container startup failures, high resource usage, or crashed daemons.
- Managing WireGuard or Tailscale mesh connectivity across homelab nodes.
- Orchestrating health probes, automated backups, or service restarts.
- Configuring environment variables, storage mounts, and volume permissions.

---

## 1. Homelab Architecture & Service Registry

Maintain an inventory of homelab services, ports, and internal endpoints:

```
+-----------------------------------------------------------------+
|                       HOMELAB NODE: ichome                      |
|                     (IP: 192.168.1.4 / 100.111.215.107)         |
+-----------------------------------------------------------------+
| Container         | Internal Port | External Port | Service     |
|-------------------+---------------+---------------+-------------|
| forgejo_git       | 3000          | 3000          | Git Forge   |
| jellyfin_media    | 8096          | 8096          | Streaming   |
| navidrome_music   | 4533          | 4533          | Subsonic    |
| stalwart_mail     | 8080, 25, 993 | 8080, 25, 993 | Mail Server |
+-----------------------------------------------------------------+
```

---

## 2. Fast MCP Tool Definitions

Claude-homelab utilizes standardized JSON-RPC tools:

### `homelab_inspect_service`
```json
{
  "name": "homelab_inspect_service",
  "description": "Inspect container health, restart count, memory and CPU usage",
  "parameters": {
    "type": "object",
    "properties": {
      "service_name": { "type": "string", "description": "e.g., jellyfin_media" }
    },
    "required": ["service_name"]
  }
}
```

### `homelab_restart_service`
```json
{
  "name": "homelab_restart_service",
  "description": "Perform graceful restart of a homelab container with post-restart healthcheck",
  "parameters": {
    "type": "object",
    "properties": {
      "service_name": { "type": "string" },
      "timeout_seconds": { "type": "integer", "default": 30 }
    },
    "required": ["service_name"]
  }
}
```

---

## 3. Operational Workflows

### 3.1 Service Health Probing
```bash
# Verify all HTTP endpoints return HTTP 200
for port in 3000 8096 4533 8080; do
  code=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 http://localhost:$port)
  echo "Port $port status: $code"
done
```

### 3.2 Tailscale Mesh Verification
```bash
# Check node connectivity on the mesh
tailscale status
tailscale ping 100.111.215.107
```

### 3.3 Storage & Volume Permission Fixes
```bash
# Ensure media and data permissions are non-root readable
sudo chown -R 1000:1000 /home/adhithan/media
chmod -R u=rwX,go=rX /home/adhithan/media
```
