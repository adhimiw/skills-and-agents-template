---
name: frigate-nvr
description: >-
  Production-grade Frigate NVR configuration, homelab deployment, and hardware-accelerated surveillance automation. Covers real-time RTSP/WebRTC camera streaming with go2rtc, Coral TPU and GPU hardware acceleration, Docker Compose homelab deployment, motion zones and masking, MQTT event streaming, and Home Assistant integration. Triggers: 'frigate', 'nvr', 'coral tpu', 'rtsp stream', 'go2rtc', 'motion zones', 'camera detection', 'surveillance camera', 'object detection nvr'.
---

# Frigate NVR & Real-Time Surveillance Engine

Production guide for deploying, configuring, and maintaining Frigate NVR on homelabs and edge servers. Covers zero-lag camera streaming, low-power TPU/GPU object detection, fine-grained spatial zones, and MQTT event pipelines.

## Triggers & Activation Matrix

Activate this skill when:
- Deploying or upgrading Frigate NVR in Docker/Kubernetes on bare metal, Proxmox, or unRAID.
- Configuring Google Coral Edge TPU (USB, M.2, PCIe) or Intel/NVIDIA hardware acceleration.
- Architecting low-latency camera streaming using go2rtc (WebRTC, MSE, RTSP restreaming).
- Creating or tuning motion masks, detection zones, min/max object sizes, and false positive filters.
- Integrating camera events into MQTT, Home Assistant, Node-RED, or custom automation hooks.
- Troubleshooting stream dropouts, `ffmpeg` crashes, high CPU/SHM usage, or detector detachments.

---

## 1. System Architecture

```
[ IP Cameras / Doorbell ]
          │ RTSP (Main & Sub Streams)
          ▼
    ┌───────────┐
    │  go2rtc   │ ◄── Restreams (WebRTC, MSE, RTSP) ──► Home Assistant / Web UI
    └─────┬─────┘
          │ Internal RTSP pipe
          ▼
   ┌──────────────┐
   │ FFmpeg Ingest│ ──► Hardware Decoder (VA-API / NVDEC / QuickSync)
   └──────┬───────┘
          │
     ┌────┴─────────────────────────────┐
     ▼                                  ▼
[ Motion Detector ] (CPU, lightweight) [ Audio Detector ]
     │ Triggered bounding box
     ▼
[ Object Detector ] ──► Google Coral Edge TPU / OpenVINO / TensorRT
     │ Verified labels ('person', 'car', 'dog', etc.)
     ▼
[ Event Engine ] ────► MQTT Broker (`frigate/events`)
     │                └─► Home Assistant / Webhooks / Notification Bot
     ▼
[ Recording & Snapshots ] ──► Local Storage / NAS (`/media/frigate`)
```

### Stream Role Separation
- **Detect stream**: Low resolution (e.g., 720p or 640x360), 5–7 fps. Feeds the motion and object detection pipeline. Keeps CPU and TPU overhead minimal.
- **Record stream**: High resolution (1080p, 2K, or 4K), 15–30 fps. Streamed directly to disk using `preset-rtsp-restream` with no re-encoding.

---

## 2. Homelab Docker Deployment

### Shared Memory (SHM) Formula
Frigate requires shared memory for frame passing between processes. Calculate required SHM before writing the Compose file:

$$\text{SHM Size} = (\text{Cameras}) \times (\text{Detect Width} \times \text{Detect Height} \times 1.5 \times 9) + 270\text{MB}$$

*Example: 4 cameras @ 1280x720 detect resolution = ~350MB $\rightarrow$ allocate `shm_size: "512m"` or `"1g"`.*

### `docker-compose.yml`

```yaml
version: "3.9"

services:
  frigate:
    container_name: frigate
    privileged: true # Required for certain Coral PCIe/USB and /dev/dri mappings
    restart: unless-stopped
    image: ghcr.io/blakeblackshear/frigate:stable
    shm_size: "1024m" # Adjust based on camera count & resolution
    devices:
      # Hardware Acceleration (Intel QuickSync / VA-API)
      - /dev/dri/renderD128:/dev/dri/renderD128
      # Google Coral USB TPU (bus mapping)
      - /dev/bus/usb:/dev/bus/usb
      # Google Coral M.2 / PCIe (uncomment if applicable)
      # - /dev/apex_0:/dev/apex_0
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /opt/frigate/config:/config
      - /mnt/storage/frigate:/media/frigate
      # RAM disk for temporary clip caching to save SSD wear
      - type: tmpfs
        target: /tmp/cache
        tmpfs:
          size: 1000000000 # 1GB RAM cache
    ports:
      - "5000:5000"       # Frigate Web UI & API
      - "8554:8554"       # RTSP Restream (go2rtc)
      - "8555:8555/tcp"   # WebRTC over TCP
      - "8555:8555/udp"   # WebRTC over UDP
    environment:
      - FRIGATE_RTSP_PASSWORD=super_secret_camera_token
      - PLUS_API_KEY="" # Optional Frigate+ key
```

---

## 3. Production Configuration (`/config/config.yml`)

```yaml
mqtt:
  enabled: true
  host: 192.168.1.50
  port: 1883
  user: mqtt_frigate
  password: mqtt_secure_password
  topic_prefix: frigate
  client_id: frigate_nvr

# Hardware Detectors Configuration
detectors:
  coral_usb:
    type: edgetpu
    device: usb
  # Alternative PCIe Coral:
  # coral_pci:
  #   type: edgetpu
  #   device: pci
  # Alternative OpenVINO (Intel CPU/iGPU) fallback:
  # ov_detector:
  #   type: openvino
  #   device: GPU # or CPU

# Unified Stream Ingest & Live View Server
go2rtc:
  streams:
    front_door:
      - rtsp://admin:CameraPass123@192.168.1.101:554/Streaming/Channels/101 # 4K Main
    front_door_sub:
      - rtsp://admin:CameraPass123@192.168.1.101:554/Streaming/Channels/102 # 720p Sub
    backyard:
      - rtsp://admin:CameraPass123@192.168.1.102:554/h264Preview_01_main
    backyard_sub:
      - rtsp://admin:CameraPass123@192.168.1.102:554/h264Preview_01_sub

cameras:
  front_door:
    ffmpeg:
      hwaccel_args: preset-vaapi # or preset-nvidia-h264
      inputs:
        # Detect stream (Sub-stream: low resolution, low fps)
        - path: rtsp://127.0.0.1:8554/front_door_sub
          input_args: preset-rtsp-restream
          roles:
            - detect
        # Record stream (Main stream: high resolution)
        - path: rtsp://127.0.0.1:8554/front_door
          input_args: preset-rtsp-restream
          roles:
            - record

    detect:
      enabled: true
      width: 1280
      height: 720
      fps: 5

    objects:
      track:
        - person
        - car
        - dog
        - cat
      filters:
        person:
          min_score: 0.65
          threshold: 0.75
          min_area: 5000
          max_area: 150000

    # Motion Mask: ignore trees, sky, timestamp to prevent false triggers
    motion:
      mask:
        - 0,0,1280,0,1280,80,0,80 # Mask top camera timestamp bar
        - 950,100,1280,100,1280,450,950,300 # Mask swaying tree branches

    # Spatial Detection Zones
    zones:
      driveway:
        coordinates: 120,710,1240,710,890,320,380,320
        objects:
          - car
          - person
      porch:
        coordinates: 380,320,890,320,850,150,410,150
        objects:
          - person
        inertia: 3
        loitering_time: 2

    record:
      enabled: true
      retain:
        days: 3
        mode: all # Continuous 24/7 record
      events:
        retain:
          default: 14 # Keep event clips for 14 days
          mode: active_objects
        pre_capture: 5
        post_capture: 10

    snapshots:
      enabled: true
      clean_copy: true
      timestamp: true
      bounding_box: true
      retain:
        default: 14
```

---

## 4. Motion Zones, Masking, and Coordinate Tuning

Frigate checks two layers of boundaries:
1. **Motion Mask (`motion.mask`)**: Pixels masked here are entirely ignored during motion analysis. Used for static noise, cloud shadows, tree leaves, and OSD timestamps.
2. **Detection Zone (`zones.<name>`)**: Active areas where verified objects trigger events. Evaluated using the **bottom-center point** of the detected object's bounding box.

### Coordinate Generation Workflow
Frigate uses normalized coordinates $(0 \text{ to } 1)$ or direct resolution coordinates $(X, Y)$ relative to the `detect` stream resolution.

1. Fetch a current reference frame:
   ```bash
   curl -o /tmp/frame.jpg "http://localhost:5000/api/front_door/latest.jpg?h=720"
   ```
2. Open Frigate Web UI $\rightarrow$ **Settings** $\rightarrow$ **Masks & Zones**.
3. Use the visual editor to click polygon points and copy the generated coordinate array.
4. Paste directly into `config.yml` and trigger a live reload:
   ```bash
   curl -X POST "http://localhost:5000/api/config/reload"
   ```

---

## 5. MQTT Event Streaming & Automation

### Topic Topology
- `frigate/events`: Continuous JSON stream containing lifecycle states (`new`, `update`, `end`).
- `frigate/<camera_name>/<object_name>`: Count of active tracked objects.
- `frigate/<camera_name>/motion`: Binary motion status (`ON`/`OFF`).
- `frigate/<zone_name>/<object_name>`: Object presence inside designated zone.

### Event Payload Schema (`frigate/events`)
```json
{
  "before": {
    "id": "1730650000.123456-abc123",
    "camera": "front_door",
    "label": "person",
    "top_score": 0.82,
    "current_zones": ["driveway"],
    "entered_zones": ["driveway"],
    "has_snapshot": false,
    "has_clip": false
  },
  "after": {
    "id": "1730650000.123456-abc123",
    "camera": "front_door",
    "label": "person",
    "top_score": 0.89,
    "current_zones": ["porch"],
    "entered_zones": ["driveway", "porch"],
    "has_snapshot": true,
    "has_clip": true
  },
  "type": "update"
}
```

### Python Real-Time Event Listener
Use this script to trigger webhook notifications, push notifications, or custom agent actions:

```python
#!/usr/bin/env python3
import json
import urllib.request
import paho.mqtt.client as mqtt

FRIGATE_HOST = "http://127.0.0.1:5000"
MQTT_BROKER = "192.168.1.50"
MQTT_TOPIC = "frigate/events"

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))
    event_type = payload.get("type")
    after = payload.get("after", {})
    
    # Trigger alert when person enters 'porch' zone
    if "porch" in after.get("current_zones", []) and after.get("label") == "person":
        event_id = after.get("id")
        camera = after.get("camera")
        score = after.get("top_score")
        print(f"[ALERT] Person detected on {camera} (Confidence: {score:.2f})")
        
        # Snapshot URL
        snapshot_url = f"{FRIGATE_HOST}/api/events/{event_id}/snapshot.jpg"
        print(f"Snapshot available at: {snapshot_url}")

client = mqtt.Client(client_id="frigate_agent_listener")
client.on_message = on_message
client.connect(MQTT_BROKER, 1883, 60)
client.subscribe(MQTT_TOPIC)
print("Listening for Frigate surveillance events...")
client.loop_forever()
```

---

## 6. Error Recovery & Diagnostics Matrix

| Symptom / Error | Root Cause | Diagnosis Command | Remediation |
|---|---|---|---|
| `No Edge TPU was detected` | USB unbind, power brownout, or missing driver/device pass-through | `lsusb \| grep -i "Google"` or `lspci \| grep -i "0863"` | 1. Ensure USB 3.0 port with adequate power (Coral spikes to 2A).<br>2. In Docker, pass `/dev/bus/usb` or `/dev/apex_0`.<br>3. Reset USB bus: `sudo usbreset "Google Inc."`. |
| `ffmpeg exited with code 1` or repeated reconnects | RTSP transport mismatch, corrupt packet stream, or bad credentials | `docker logs frigate --tail 100 \| grep ffmpeg` | 1. In `go2rtc`, force TCP: `rtsp://user:pass@IP:554/stream#transport=tcp`.<br>2. Add `preset-rtsp-generic` to input args. |
| Container crash with `Bus error` or `SIGBUS` | `/dev/shm` shared memory exhausted | `df -h /dev/shm` inside container | Increase `shm_size` in `docker-compose.yml` (e.g. from `256m` to `1024m` or `2048m`). |
| 100% CPU on all cores | Detect role assigned to 4K stream instead of sub-stream; HW decode missing | `curl -s http://localhost:5000/api/stats \| jq .cpu_usages` | 1. Map `detect` role strictly to 720p/360p sub-stream.<br>2. Verify `hwaccel_args: preset-vaapi` is active (`vainfo`). |
| False positive spam (car, person on stationary bushes) | Motion threshold too low or missing `min_area` | Inspect false snapshots in Web UI event log | 1. Increase `min_score` and `threshold` to `0.75+`.<br>2. Add `min_area` filter.<br>3. Add `motion.mask` over foliage. |
| WebRTC live stream fails to load outside LAN | Missing STUN/TURN or blocked UDP port | Browser DevTools WebRTC internals (`chrome://webrtc-internals`) | Open UDP port `8555` on firewall. Configure `go2rtc.webrtc.candidates` with public IP or domain. |

---

## 7. Verification & Health Check Commands

Execute these verification commands after deployment:

```bash
# 1. Verify Frigate API & detector performance
curl -s http://localhost:5000/api/version
curl -s http://localhost:5000/api/stats | jq '{
  detectors: .detectors,
  fps: [.cameras[] | {name: .name, camera_fps: .camera_fps, process_fps: .process_fps, detection_fps: .detection_fps}],
  service: .service
}'

# 2. Check Coral TPU inference speed (Expected: 8-15ms for Coral, 80-200ms for CPU)
curl -s http://localhost:5000/api/stats | jq '.detectors.coral_usb.inference_speed'

# 3. Test camera RTSP feed directly via ffprobe
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 "rtsp://127.0.0.1:8554/front_door"

# 4. Monitor real-time MQTT events
mosquitto_sub -h 192.168.1.50 -t "frigate/events" -v
```
