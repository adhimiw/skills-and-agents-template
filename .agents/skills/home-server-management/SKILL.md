---
name: home-server-management
description: Manage homelab infrastructure and home servers. Use for Docker compose lifecycle orchestration, container health checks, automated disk space pruning, storage health monitoring via SMART, backup automation with Restic/Borg/Rclone, and systemd log rotation.
---

# Home Server & Homelab Management

## Overview

`home-server-management` provides operational runbooks, systemd service templates, and automation scripts for running resilient, low-maintenance home servers and homelabs. Based on best practices from `mcpmarket/home-server-management` and `modbender-home-server`, this skill covers declarative Docker container orchestration, automated disk pruning, predictive hardware drive failure monitoring (S.M.A.R.T.), scheduled encrypted backups, and system log hygiene.

---

## Triggers & When to Use

Activate this skill when:
- Deploying, updating, or debugging Docker Compose stacks in a home server.
- Configuring automated health checks and auto-restart policies for homelab services.
- Reclaiming disk space and resolving full root (`/`) or storage volume issues.
- Monitoring hard drive and NVMe health via S.M.A.R.T. (`smartctl`, `smartd`).
- Establishing automated backup routines for Docker volumes and databases (Postgres, SQLite) using Restic, Borg, or Rclone.
- Managing log sprawl, configuring Docker log limits, or tuning systemd `journald`.
- Diagnosing OOM killer events, hung containers, or network port conflicts.

---

## 1. Directory Structure & Stack Conventions

Standardize homelab services under `/opt/stacks` or `/home/$USER/stacks` for reproducible deployment:

```
/opt/stacks/
├── docker-compose@.service       # Global systemd template for stack management
├── media/
│   ├── docker-compose.yml
│   └── .env                      # Non-versioned secrets and paths
├── monitoring/
│   ├── docker-compose.yml
│   └── prometheus.yml
└── scripts/
    ├── backup.sh
    └── disk-prune.sh
```

---

## 2. Docker Compose Lifecycle Management

### 2.1 Production-Grade Service Template
Every container stack should include logging limits, resource constraints, health checks, and non-root users:

```yaml
# /opt/stacks/example/docker-compose.yml
services:
  app:
    image: example/app:1.4.0
    container_name: example_app
    restart: unless-stopped
    user: "1000:1000"
    environment:
      - TZ=America/New_York
      - DATABASE_URL=postgres://${DB_USER}:${DB_PASS}@db:5432/${DB_NAME}
    env_file:
      - .env
    volumes:
      - /opt/stacks/example/data:/data:rw
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "127.0.0.1:8080:8080" # Bind to loopback; reverse proxy handles TLS
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 2048M
        reservations:
          memory: 512M
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
        max-file: "3"
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 20s
```

### 2.2 Systemd Integration for Auto-Starting Stacks
Create a systemd template unit to manage compose stacks as native system services:

```ini
# /etc/systemd/system/docker-compose@.service
[Unit]
Description=Docker Compose Stack - %i
Requires=docker.service
After=docker.service network-online.target
Wants=network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/stacks/%i
ExecStart=/usr/bin/docker compose up -d --remove-orphans
ExecStop=/usr/bin/docker compose down
ExecReload=/usr/bin/docker compose pull && /usr/bin/docker compose up -d

[Install]
WantedBy=multi-user.target
```

Enable and start any stack with:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now docker-compose@media
sudo systemctl status docker-compose@media
```

### 2.3 Safe Stack Updates
```bash
# Pull new images, check diffs, and recreate containers idempotently
cd /opt/stacks/media
docker compose pull
docker compose up -d --remove-orphans
docker image prune -f
```

---

## 3. Container Health & Auto-Healing

### 3.1 Monitoring Unhealthy Containers
```bash
# List all unhealthy containers across all stacks
docker ps --filter health=unhealthy --format "table {{.Names}}\t{{.Status}}\t{{.RunningFor}}"

# Inspect health check failure logs
docker inspect --format='{{json .State.Health}}' example_app | jq
```

### 3.2 Autoheal Container
Deploy `willfarrell/autoheal` to automatically restart containers whose health checks fail:

```yaml
services:
  autoheal:
    image: willfarrell/autoheal:latest
    container_name: autoheal
    restart: unless-stopped
    environment:
      - AUTOHEAL_CONTAINER_LABEL=all
      - AUTOHEAL_INTERVAL=30
      - AUTOHEAL_START_PERIOD=60
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

---

## 4. Automated Disk Pruning & Maintenance

Homelabs frequently face storage exhaustion from dangling Docker images, build caches, and old apt kernels.

### 4.1 Safe Disk Pruning Script
Create `/usr/local/bin/homelab-prune.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "=== [$(date)] Starting Homelab Disk Pruning ==="

# 1. Prune unused Docker images older than 7 days, networks, and build caches (keeps named volumes)
echo "Pruning Docker system..."
docker system prune -af --filter "until=168h"
docker builder prune -af --filter "until=168h"

# 2. Clean apt package manager cache
if command -v apt-get &>/dev/null; then
    echo "Cleaning APT caches..."
    apt-get autoremove --purge -y
    apt-get clean
fi

# 3. Vacuum systemd journal logs keeping only the last 7 days or 1 GB
echo "Vacuuming systemd journal..."
journalctl --vacuum-time=7d
journalctl --vacuum-size=1G

# 4. Report disk usage
echo "Current Filesystem Usage:"
df -hT --exclude-type=tmpfs --exclude-type=overlay --exclude-type=squashfs
```

Make executable and schedule weekly via cron or systemd timer:
```bash
sudo chmod +x /usr/local/bin/homelab-prune.sh
# Run every Sunday at 03:00 AM
echo "0 3 * * 0 root /usr/local/bin/homelab-prune.sh >> /var/log/homelab-prune.log 2>&1" | sudo tee /etc/cron.d/homelab-prune
```

---

## 5. Storage Health & S.M.A.R.T. Monitoring

Proactively detect failing hard drives and NVMe SSDs before unrecoverable data loss occurs.

### 5.1 CLI Disk Diagnostics
```bash
# List all attached storage devices
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT,MODEL

# Check SMART health summary for SATA/SAS HDD or SSD
sudo smartctl -H /dev/sda

# View detailed attributes (watch: Reallocated_Sector_Ct, Current_Pending_Sector, UDMA_CRC_Error_Count)
sudo smartctl -A /dev/sda

# NVMe drive health (watch: percentage_used, media_errors, critical_warning)
sudo nvme smart-log /dev/nvme0

# Run a non-disruptive SMART short self-test
sudo smartctl -t short /dev/sda
# Check test progress/result
sudo smartctl -l selftest /dev/sda
```

### 5.2 Automated Continuous SMART Daemon (`smartd`)
Configure `/etc/smartd.conf` to monitor all drives, test weekly, and send alerts:

```conf
# /etc/smartd.conf
# -a: monitor all standard SMART attributes
# -o on: enable automatic offline testing
# -S on: enable attribute autosave
# -s (S/../../7/02|L/../../7/04): Short test every Sunday at 2am, Long test every Sunday at 4am
# -m: alert email or webhook forwarder script
# -M exec: custom notification script
DEVICESCAN -d removable -n standby -a -o on -S on -s (S/../../7/02|L/../../7/04) -m root -M exec /usr/local/bin/smart-notify.sh
```

Enable the daemon:
```bash
sudo systemctl enable --now smartmontools
```

### 5.3 ZFS / Btrfs Pool Scrubbing
For systems using ZFS or Btrfs, schedule periodic data integrity scrubs:
```bash
# ZFS pool health check
zpool status -x
# Start background scrub
zpool scrub tank

# Btrfs scrub
btrfs scrub start /mnt/storage
btrfs scrub status /mnt/storage
```

---

## 6. Automated Backup Scheduling Strategy

Follow the 3-2-1 backup strategy: 3 copies of data, on 2 different media, 1 stored offsite.

### 6.1 Database Dump Before Backup
Never backup live database files (`/var/lib/postgresql/data`) directly; generate consistent logical dumps:

```bash
# Dump Postgres container database
docker exec -t postgres_db pg_dumpall -U postgres | gzip > /opt/backups/dumps/postgres_$(date +%Y%m%d).sql.gz

# Dump SQLite database with vacuum
sqlite3 /opt/stacks/vaultwarden/data/db.sqlite3 ".backup '/opt/backups/dumps/vaultwarden_$(date +%Y%m%d).sqlite3'"
```

### 6.2 Encrypted Incremental Backups with Restic
Restic deduplicates, encrypts, and supports local mounts, SFTP, and cloud object stores (S3, B2).

```bash
# 1. Initialize Restic repository on secondary drive or NAS
export RESTIC_REPOSITORY="/mnt/nas/backups/homelab"
export RESTIC_PASSWORD_FILE="/etc/restic-password.txt"
restic init

# 2. Automated backup script: /usr/local/bin/homelab-backup.sh
```

```bash
#!/usr/bin/env bash
set -euo pipefail

export RESTIC_REPOSITORY="/mnt/nas/backups/homelab"
export RESTIC_PASSWORD_FILE="/etc/restic-password.txt"

echo "Dumping databases..."
mkdir -p /opt/backups/dumps
docker exec -t postgres_db pg_dump -U postgres app_db > /opt/backups/dumps/app_db.sql

echo "Running Restic backup..."
restic backup \
  --exclude-caches \
  --exclude="**/.cache" \
  --exclude="**/node_modules" \
  /opt/stacks \
  /opt/backups/dumps

echo "Applying retention policy..."
restic forget \
  --keep-daily 7 \
  --keep-weekly 4 \
  --keep-monthly 12 \
  --prune

echo "Backup complete: $(date)"
```

### 6.3 Systemd Timer Configuration
```ini
# /etc/systemd/system/homelab-backup.timer
[Unit]
Description=Nightly Homelab Backup Timer

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable with `sudo systemctl enable --now homelab-backup.timer`.

---

## 7. System Log Hygiene & Journal Management

### 7.1 Global Docker Log Rotation
Prevent Docker from filling disk partitions with unbounded JSON container logs:

```json
// /etc/docker/daemon.json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "50m",
    "max-file": "3"
  }
}
```
Apply with `sudo systemctl restart docker`.

### 7.2 Systemd Journal Size Limits
Configure `/etc/systemd/journald.conf`:
```ini
[Journal]
Storage=persistent
SystemMaxUse=1G
RuntimeMaxUse=200M
SystemMaxFileSize=100M
MaxRetentionSec=14day
```
Apply with `sudo systemctl restart systemd-journald`.

---

## 8. Emergency Troubleshooting Playbooks

### Problem: Docker Container Stuck in Terminating / Cannot Kill
```bash
# 1. Force kill container
docker kill <container_name>

# 2. If stuck in "removal in progress", find remaining containerd task
sudo pkill -9 -f "containerd-shim.*<container_id>"

# 3. Restart docker daemon cleanly
sudo systemctl restart docker
```

### Problem: Out-Of-Memory (OOM) Killer Triggered
```bash
# Check if kernel OOM killer was invoked
dmesg -T | grep -i oom
journalctl -k -b | grep -i -E "killed process|oom_reaper"

# Identify top memory-consuming containers
docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}"
```

### Problem: Port Conflict on Service Start
```bash
# Identify process holding the target port (e.g., port 80)
sudo ss -tulpn | grep :80
# Or using lsof
sudo lsof -i :80
```
