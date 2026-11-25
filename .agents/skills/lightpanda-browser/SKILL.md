---
name: lightpanda-browser
description: >-
  Ultra-fast, low-memory Zig-based headless browser automation for AI agents. Covers Lightpanda binary and Docker setup, Chrome DevTools Protocol (CDP) integration with Puppeteer and Playwright, high-throughput web scraping without Chromium overhead, DOM and Markdown extraction, and dual-browser fallback patterns. Triggers: 'lightpanda', 'headless browser', 'cdp scraping', 'low memory browser', 'fast browser', 'puppeteer lightpanda', 'playwright lightpanda', 'zig browser', 'agent browser'.
---

# Lightpanda Headless Browser for AI Agents

Lightpanda is an open-source, ultra-lightweight headless browser written in Zig and C, specifically designed for AI agents, LLM web scrapers, and high-concurrency automation. While standard Chromium consumes 300MB–500MB RAM per tab and takes seconds to boot, Lightpanda starts in milliseconds and maintains a ~20MB–30MB memory footprint while exposing a standard Chrome DevTools Protocol (CDP) interface.

## Triggers & Activation Matrix

Activate this skill when:
- Executing fast, high-concurrency web scraping or content extraction in AI agent workflows.
- Running headless browsing on memory-constrained machines, small VPS instances, or container swarms.
- Connecting AI agents to browser sessions via Puppeteer, Playwright, or direct WebSocket CDP.
- Rendering dynamic, JavaScript-heavy Single Page Applications (SPAs) without Chromium's resource tax.
- Converting live web pages to clean Markdown or DOM structures for LLM context injection.
- Setting up a dual-engine architecture: Lightpanda as the primary high-speed engine with Chromium fallback.

---

## 1. Chromium vs. Lightpanda Architecture

| Feature | Standard Chromium | Lightpanda Browser |
|---|---|---|
| **Language** | C++ (~35M lines) | Zig / C |
| **Startup Latency** | 800ms – 2500ms | 5ms – 25ms |
| **RAM per Instance** | 250MB – 600MB | 15MB – 35MB |
| **Max Concurrent Sessions (8GB RAM)** | ~12 – 18 instances | 200+ instances |
| **Protocol** | Full Chrome DevTools Protocol (CDP) | Subset of core automation CDP |
| **Primary Target** | Human visual rendering, WebGL, media | AI agents, scraping, data pipelines |

### Decision Guide: When to Use Lightpanda vs. Full Chromium
- **Use Lightpanda**: Text extraction, dynamic SPAs (React, Vue, Next.js), scraping behind client-side rendering, form filling, automated search queries, agent tool calls.
- **Fall Back to Full Chromium**: Heavy WebGL / Canvas games, WebRTC video streaming, extension loading, sites requiring complex Widevine DRM.

---

## 2. Installation & Daemon Deployment

### Option A: Standalone Binary (Linux x86_64 / ARM64)
```bash
# Download latest release
curl -fsSL https://github.com/lightpanda-io/browser/releases/latest/download/lightpanda-linux-x86_64.tar.gz -o /tmp/lightpanda.tar.gz
sudo tar -xzf /tmp/lightpanda.tar.gz -C /usr/local/bin/
sudo chmod +x /usr/local/bin/lightpanda

# Start the CDP server
lightpanda serve --host 127.0.0.1 --port 9222
```

### Option B: Docker Container (Recommended for Homelab & Production)
```bash
docker run -d \
  --name lightpanda \
  --restart unless-stopped \
  -p 9222:9222 \
  ghcr.io/lightpanda-io/browser:latest \
  lightpanda serve --host 0.0.0.0 --port 9222
```

### Option C: Systemd Service (`/etc/systemd/system/lightpanda.service`)
```ini
[Unit]
Description=Lightpanda Headless Browser Service
After=network.target

[Service]
Type=simple
User=adhithan
ExecStart=/usr/local/bin/lightpanda serve --host 127.0.0.1 --port 9222
Restart=always
RestartSec=3
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

---

## 3. CDP Integration Workflows

Lightpanda exposes a standard WebSocket CDP server at `ws://<host>:9222`.

### Playwright Integration (Python)
Playwright connects directly using `connect_over_cdp`:

```python
#!/usr/bin/env python3
import asyncio
from playwright.async_api import async_playwright

async def run_lightpanda_scrape(url: str):
    async with async_playwright() as p:
        # Connect to Lightpanda over CDP
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="domcontentloaded")
        
        # Extract title and body
        title = await page.title()
        content = await page.inner_text("body")
        
        print(f"Page Title: {title}")
        print(f"Extracted {len(content)} characters of text.")
        
        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_lightpanda_scrape("https://news.ycombinator.com"))
```

### Puppeteer Integration (Node.js)
```javascript
import puppeteer from 'puppeteer-core';

async function main() {
  const browser = await puppeteer.connect({
    browserWSEndpoint: 'ws://127.0.0.1:9222',
    defaultViewport: { width: 1280, height: 800 }
  });

  const page = await browser.newPage();
  await page.goto('https://en.wikipedia.org/wiki/Artificial_intelligence', {
    waitUntil: 'domcontentloaded'
  });

  const heading = await page.$eval('h1#firstHeading', el => el.textContent);
  console.log('Heading:', heading);

  await page.close();
  await browser.disconnect();
}

main().catch(console.error);
```

### Zero-Dependency Agent Client (Direct Python WebSocket)
For maximum speed without npm or Playwright overhead, communicate via raw JSON-RPC over WebSockets:

```python
#!/usr/bin/env python3
import json
import asyncio
import websockets
import urllib.request

CDP_HTTP = "http://127.0.0.1:9222"

async def fast_agent_fetch(target_url: str):
    # 1. Fetch version and WebSocket endpoint
    req = urllib.request.urlopen(f"{CDP_HTTP}/json/version")
    info = json.loads(req.read().decode())
    ws_url = info["webSocketDebuggerUrl"]

    async with websockets.connect(ws_url) as ws:
        # Create target page
        await ws.send(json.dumps({
            "id": 1,
            "method": "Target.createTarget",
            "params": {"url": "about:blank"}
        }))
        res = json.loads(await ws.recv())
        target_id = res["result"]["targetId"]

        # Connect to specific target
        page_ws_url = f"ws://127.0.0.1:9222/devtools/page/{target_id}"
        async with websockets.connect(page_ws_url) as page_ws:
            # Enable Page domain
            await page_ws.send(json.dumps({"id": 2, "method": "Page.enable"}))
            await page_ws.recv()

            # Navigate
            await page_ws.send(json.dumps({
                "id": 3,
                "method": "Page.navigate",
                "params": {"url": target_url}
            }))
            
            # Wait for load event
            while True:
                msg = json.loads(await page_ws.recv())
                if msg.get("method") == "Page.loadEventFired":
                    break

            # Evaluate JS to dump text content
            await page_ws.send(json.dumps({
                "id": 4,
                "method": "Runtime.evaluate",
                "params": {"expression": "document.body.innerText"}
            }))
            eval_res = json.loads(await page_ws.recv())
            text = eval_res["result"]["result"]["value"]
            return text

if __name__ == "__main__":
    result = asyncio.run(fast_agent_fetch("https://example.com"))
    print("Fetched text snippet:", result[:200])
```

---

## 4. High-Throughput Scraper & Markdown Converter

AI agents frequently require web pages converted to clean, token-efficient Markdown. This recipe batches URLs concurrently through Lightpanda:

```python
#!/usr/bin/env python3
import asyncio
from playwright.async_api import async_playwright

HTML2MARKDOWN_JS = """
() => {
    // Basic DOM to Markdown converter inside page context
    const clean = (el) => {
        let text = '';
        for (let node of el.childNodes) {
            if (node.nodeType === 3) {
                text += node.textContent.trim() + ' ';
            } else if (node.nodeType === 1) {
                const tag = node.tagName.toLowerCase();
                if (['script', 'style', 'nav', 'footer', 'noscript'].includes(tag)) continue;
                if (/^h[1-6]$/.test(tag)) {
                    const level = '#'.repeat(parseInt(tag[1]));
                    text += `\\n\\n${level} ${node.innerText.trim()}\\n\\n`;
                } else if (tag === 'p') {
                    text += `\\n\\n${node.innerText.trim()}\\n\\n`;
                } else if (tag === 'li') {
                    text += `\\n* ${node.innerText.trim()}`;
                } else {
                    text += clean(node);
                }
            }
        }
        return text;
    };
    return clean(document.body).replace(/\\n{3,}/g, '\\n\\n');
}
"""

async def scrape_to_markdown(url: str, browser):
    context = await browser.new_context()
    page = await context.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=8000)
        markdown = await page.evaluate(HTML2MARKDOWN_JS)
        title = await page.title()
        return {"url": url, "title": title, "markdown": markdown.strip(), "status": "ok"}
    except Exception as e:
        return {"url": url, "error": str(e), "status": "failed"}
    finally:
        await context.close()

async def batch_scrape(urls: list[str]):
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        tasks = [scrape_to_markdown(u, browser) for u in urls]
        results = await asyncio.gather(*tasks)
        await browser.close()
        return results

if __name__ == "__main__":
    urls = [
        "https://news.ycombinator.com",
        "https://github.com/trending",
        "https://arxiv.org/abs/2312.00752"
    ]
    data = asyncio.run(batch_scrape(urls))
    for item in data:
        print(f"[{item['status'].upper()}] {item['url']} -> {len(item.get('markdown', ''))} chars")
```

---

## 5. Dual-Browser Failover Pattern

Because Lightpanda implements the most crucial subsets of the web platform rather than every single obscure API, production agents should employ an automated failover loop:

```python
async def resilient_agent_fetch(url: str):
    """
    Tier 1: Try Lightpanda (20x faster, ~20MB RAM).
    Tier 2: If Lightpanda fails on rendering or missing API, fall back to Chromium.
    """
    async with async_playwright() as p:
        # 1. Attempt Lightpanda
        try:
            lp_browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
            page = await lp_browser.new_page()
            await page.goto(url, wait_until="domcontentloaded", timeout=5000)
            content = await page.inner_text("body")
            await lp_browser.close()
            if len(content.strip()) > 100:
                return {"engine": "lightpanda", "content": content}
        except Exception as lp_err:
            print(f"[Fallback Warning] Lightpanda execution failed: {lp_err}. Escalating to Chromium...")

        # 2. Fallback to Full Chromium
        ch_browser = await p.chromium.launch(headless=True)
        ch_page = await ch_browser.new_page()
        await ch_page.goto(url, wait_until="networkidle", timeout=15000)
        content = await ch_page.inner_text("body")
        await ch_browser.close()
        return {"engine": "chromium_fallback", "content": content}
```

---

## 6. Error Recovery & Diagnostics Matrix

| Issue / Error | Root Cause | Diagnosis Command | Remediation |
|---|---|---|---|
| `Connection refused: 127.0.0.1:9222` | Lightpanda daemon is not running or crashed | `ps aux \| grep lightpanda` or `curl http://127.0.0.1:9222/json/version` | Start daemon via `lightpanda serve --host 127.0.0.1 --port 9222` or restart systemd/docker. |
| `Method Page.addScriptToEvaluateOnNewDocument not supported` | Puppeteer / Playwright called a CDP method not yet in Lightpanda | Inspect debug logs from CDP client | 1. Avoid invoking unsupported CDP hooks.<br>2. Inject scripts after navigation via `page.evaluate()` rather than preload hooks.<br>3. Trigger dual-browser fallback. |
| Page returns blank white body on complex SPA | Client-side routing requires unsupported Web API (e.g. WebGL/WebGPU) | `curl -s http://127.0.0.1:9222/json/list` | Check console logs via CDP listener. If WebGL is mandatory, route that domain to Chromium. |
| Memory leak after thousands of runs | Contexts or targets left open without calling `close()` | `lsof -p $(pgrep lightpanda) \| grep -i tcp` | Ensure all scripts call `page.close()` and `context.close()` inside a `finally:` block. |
| Cloudflare Turnstile / Captcha block | Missing realistic browser fingerprint or TLS characteristics | Page innerText contains "Verifying you are human" | Configure randomized User-Agent and viewport; if blocked by TLS fingerprint, route through residential proxy or full browser harness. |

---

## 7. Verification & Health Check

```bash
# 1. Check Lightpanda version and CDP readiness
curl -s http://127.0.0.1:9222/json/version | jq .

# 2. Check active tabs/targets
curl -s http://127.0.0.1:9222/json/list | jq .

# 3. Create and close an ephemeral target
TARGET_ID=$(curl -s -X PUT http://127.0.0.1:9222/json/new?https://example.com | jq -r .id)
echo "Opened target: $TARGET_ID"
curl -s http://127.0.0.1:9222/json/close/$TARGET_ID
```
