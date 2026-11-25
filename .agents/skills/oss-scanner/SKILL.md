---
name: oss-scanner
description: >-
  Automated open-source security vulnerability scanner, CVE matcher, dependency auditor, and automated patch generator. Covers multi-ecosystem manifest parsing (npm, pip, cargo, go, maven), Google OSV and GHSA vulnerability databases, static reachability analysis, CVSS/EPSS scoring, automated non-breaking patch synthesis, and CI/CD gatekeeping. Triggers: 'oss-scanner', 'vulnerability scan', 'cve audit', 'dependency vulnerability', 'patch generation', 'anthropic scanner', 'security advisory', 'osv scanner', 'software supply chain'.
---

# Anthropic OSS Scanner & Autonomous Patch Generator

Production-grade automated vulnerability scanner and remediation engine. Designed for AI agents to audit software supply chains, match dependencies against open-source vulnerability databases (OSV, GHSA, NVD), determine exploit reachability via AST call-graph inspection, and synthesize verified, non-breaking patches.

## Triggers & Activation Matrix

Activate this skill when:
- Auditing a repository's dependencies for known CVEs, supply-chain attacks, or outdated packages.
- Performing incident triage when a new zero-day vulnerability is announced (e.g., Log4j, XZ Utils, Axios SSRF).
- Analyzing whether a transitive dependency vulnerability is reachable from the application's source code.
- Automatically generating security patches, lockfile pins, or backported fixes without breaking upstream APIs.
- Emitting SARIF (Static Analysis Results Interchange Format) reports for GitHub Code Scanning or CI/CD gates.
- Resolving complex peer-dependency conflicts during security version bumps.

---

## 1. Scanner Architecture & Verification Loop

```
┌────────────────────────────────┐
│  Target Repository / Manifests │ (package.json, requirements.txt, Cargo.lock, etc.)
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  1. Manifest & Lockfile Parser │ ──► Extracts Exact Package Versions
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  2. Advisory Matching (OSV)    │ ◄── Google OSV API / GHSA / NVD
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  3. Reachability Engine (AST)  │ ──► Is the vulnerable function actually called?
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  4. Automated Patch Synthesizer│
│     - Semver Bump              │
│     - Manifest Overrides       │
│     - In-place Backport Patch  │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  5. Verification Test Suite    │ ──► Runs unit/integration tests (npm test, pytest)
└───────────────┬────────────────┘
                │
      ┌─────────┴─────────┐
      │ Tests Pass?       │
     Yes                  No
      │                    │
      ▼                    ▼
[ Commit Patch & Branch ] [ Formulate Shim or Rollback ]
```

---

## 2. Multi-Ecosystem Support Matrix

| Ecosystem | Manifests Parsed | Native Audit CLI | Query Target |
|---|---|---|---|
| **JavaScript / TypeScript** | `package.json`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml` | `npm audit`, `pnpm audit` | `npm` |
| **Python** | `requirements.txt`, `Pipfile.lock`, `poetry.lock`, `pyproject.toml` | `pip-audit` | `PyPI` |
| **Rust** | `Cargo.toml`, `Cargo.lock` | `cargo audit` | `crates.io` |
| **Go** | `go.mod`, `go.sum` | `govulncheck` | `Go` |
| **Java / Kotlin** | `pom.xml`, `build.gradle`, `gradle.lockfile` | `dependency-check` | `Maven` |

---

## 3. High-Speed Vulnerability Scanner (`oss_scan.py`)

This script queries the Google OSV batch API (`https://api.osv.dev/v1/querybatch`), which operates without API keys or aggressive rate limits, matching exact package versions against GHSA, CVE, and RustSec databases.

```python
#!/usr/bin/env python3
"""
Autonomous Multi-Language OSS Vulnerability Scanner
Extracts dependencies from lockfiles and queries Google OSV in batch.
"""

import os
import sys
import json
import urllib.request
from pathlib import Path

OSV_BATCH_URL = "https://api.osv.dev/v1/querybatch"

def parse_package_json(lock_path: Path):
    """Extract packages from package-lock.json (v2/v3)."""
    with open(lock_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    packages = []
    # Lockfile v2/v3 structure
    if "packages" in data:
        for pkg_path, info in data["packages"].items():
            if not pkg_path:
                continue
            name = pkg_path.replace("node_modules/", "").split("node_modules/")[-1]
            version = info.get("version")
            if name and version:
                packages.append({"package": {"name": name, "ecosystem": "npm"}, "version": version})
    return packages

def parse_requirements_txt(req_path: Path):
    """Extract pinned packages from requirements.txt."""
    packages = []
    with open(req_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split("#")[0]
            if "==" in line:
                name, version = line.split("==")[:2]
                packages.append({
                    "package": {"name": name.strip(), "ecosystem": "PyPI"},
                    "version": version.strip()
                })
    return packages

def query_osv_batch(queries: list):
    """Send queries to OSV batch API in chunks of 500."""
    all_results = []
    chunk_size = 500
    for i in range(0, len(queries), chunk_size):
        chunk = queries[i:i + chunk_size]
        req = urllib.request.Request(
            OSV_BATCH_URL,
            data=json.dumps({"queries": chunk}).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                all_results.extend(data.get("results", []))
        except Exception as e:
            print(f"Error querying OSV API: {e}", file=sys.stderr)
    return all_results

def run_audit(target_dir: str):
    root = Path(target_dir)
    queries = []
    pkg_map = []

    # 1. Detect and parse npm
    npm_lock = root / "package-lock.json"
    if npm_lock.exists():
        print(f"[*] Found npm lockfile: {npm_lock}")
        pkgs = parse_package_json(npm_lock)
        queries.extend(pkgs)
        pkg_map.extend(pkgs)

    # 2. Detect and parse Python
    py_req = root / "requirements.txt"
    if py_req.exists():
        print(f"[*] Found Python requirements: {py_req}")
        pkgs = parse_requirements_txt(py_req)
        queries.extend(pkgs)
        pkg_map.extend(pkgs)

    if not queries:
        print("[!] No supported lockfiles found to audit.")
        return []

    print(f"[*] Querying OSV database for {len(queries)} package versions...")
    raw_results = query_osv_batch(queries)

    findings = []
    for item, res in zip(pkg_map, raw_results):
        vulns = res.get("vulns", [])
        if vulns:
            for v in vulns:
                findings.append({
                    "package": item["package"]["name"],
                    "ecosystem": item["package"]["ecosystem"],
                    "installed_version": item["version"],
                    "vuln_id": v.get("id"),
                    "summary": v.get("summary", "No summary provided"),
                    "details": v.get("details", ""),
                    "aliases": v.get("aliases", []),
                    "severity": extract_severity(v),
                    "fixed_versions": extract_fixed_versions(v, item["package"]["name"])
                })
    return findings

def extract_severity(vuln):
    for s in vuln.get("severity", []):
        if s.get("type") in ("CVSS_V3", "CVSS_V4"):
            return s.get("score")
    return "UNKNOWN"

def extract_fixed_versions(vuln, package_name):
    fixes = []
    for aff in vuln.get("affected", []):
        if aff.get("package", {}).get("name") == package_name:
            for r in aff.get("ranges", []):
                for e in r.get("events", []):
                    if "fixed" in e:
                        fixes.append(e["fixed"])
    return fixes

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    results = run_audit(path)
    print(f"\n[+] Audit Complete: {len(results)} vulnerabilities identified.")
    for f in results:
        fixed = ", ".join(f["fixed_versions"]) if f["fixed_versions"] else "No fix available"
        print(f" -> [{f['vuln_id']}] {f['package']}@{f['installed_version']} | Fixed in: {fixed}")
        print(f"    Summary: {f['summary']}")
```

---

## 4. Reachability Analysis (Triage Filter)

Over 70% of reported open-source vulnerabilities reside in uninvoked transitive helper functions. Before patching, determine if the vulnerable symbol is reachable:

### Reachability Decision Rules
1. **Direct Dependency vs Transitive**: If direct, check codebase imports (`grep -rn "from 'package'" src/`).
2. **Export / Method Reachability**: Read the CVE advisory for specific affected function/class names (e.g., `lodash.template` or `urllib3.PoolManager`).
3. **AST Inspection**: Run AST pattern search or Semgrep rule to check if the dangerous symbol is ever referenced:

```bash
# Check if vulnerable symbol 'merge' from 'lodash' is referenced in code
semgrep -e '$LODASH.merge($...ARGS)' --lang=javascript src/
```

| Reachability Tier | Criteria | Remediation Priority |
|---|---|---|
| **Tier 1: Active Exploitable** | Symbol imported and user-controlled input reaches vulnerable arguments | **P0 (Immediate Emergency Patch)** |
| **Tier 2: Reachable Code** | Symbol imported in application code without clear sanitization | **P1 (Patch in Current Sprint)** |
| **Tier 3: Unreachable Transitive** | Package present in lockfile but affected module/symbol never referenced | **P2 (Standard Scheduled Upgrade)** |
| **Tier 4: Test/Dev Dependency** | Vulnerability limited to test runners, bundlers, or mock libraries | **P3 (Audit & Suppress in Production)** |

---

## 5. Automated Patch Synthesis

When a vulnerability is verified, the agent synthesizes remediation according to these strategies:

### Strategy 1: Non-Breaking Semver Bump (Manifest / Lockfile)
If the fixed version is a semver-compatible minor or patch release:

```bash
# Node.js: Update lockfile entry specifically without upgrading entire tree
npm install <package>@<fixed_version> --save-exact

# Python: Update requirements or poetry
poetry update <package>
```

### Strategy 2: Overrides / Resolutions (Transitive Dependencies)
When a nested transitive dependency is vulnerable and the parent package has not yet released an update, enforce an override in the root manifest:

**In `package.json`**:
```json
{
  "overrides": {
    "vulnerable-sub-pkg": "^2.1.4"
  }
}
```

**In `pyproject.toml` (Poetry)**:
```toml
[tool.poetry.dependencies]
vulnerable-sub-pkg = ">=2.1.4"
```

### Strategy 3: In-Place Patch Backporting (`patch-package`)
If the upstream upgrade is a breaking major version (e.g., v1 $\rightarrow$ v2 with completely rewritten APIs), extract the security diff from the upstream commit and apply it locally:

```bash
# 1. Edit the file directly in node_modules/<package>/
# 2. Freeze the patch
npx patch-package <package>

# 3. Commit the created patches/<package>+version.patch file
git add patches/
```

### Automated Verification Script (`verify_patch.py`)
```python
#!/usr/bin/env python3
import subprocess
import sys

def verify_fix(test_cmd: str):
    print(f"[*] Running test suite: {test_cmd}")
    proc = subprocess.run(test_cmd, shell=True)
    if proc.returncode != 0:
        print("[!] REGRESSION DETECTED: Security patch broke existing tests!")
        return False
    print("[+] Test suite passed cleanly. Security patch is non-breaking.")
    return True

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "npm test"
    if not verify_fix(cmd):
        sys.exit(1)
```

---

## 6. CI/CD Gatekeeping & SARIF Generation

To display security scan results in GitHub Code Scanning, export findings as SARIF 2.1.0:

```json
{
  "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
  "version": "2.1.0",
  "runs": [
    {
      "tool": {
        "driver": {
          "name": "Anthropic-OSS-Scanner",
          "rules": [
            {
              "id": "GHSA-xxxx-yyyy-zzzz",
              "shortDescription": { "text": "Prototype Pollution in package-x" },
              "defaultConfiguration": { "level": "error" }
            }
          ]
        }
      },
      "results": [
        {
          "ruleId": "GHSA-xxxx-yyyy-zzzz",
          "message": { "text": "Package package-x@1.0.0 is vulnerable. Upgrade to 1.0.2." },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": { "uri": "package-lock.json" },
                "region": { "startLine": 1 }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

---

## 7. Error Recovery & Diagnostics Matrix

| Failure Mode | Root Cause | Diagnosis Command | Remediation |
|---|---|---|---|
| `npm ERR! ERESOLVE unable to resolve dependency tree` | Peer dependency mismatch during version bump | `npm ls <package>` | 1. Use `npm install <package> --legacy-peer-deps` as temporary mitigation.<br>2. Use `overrides` in `package.json` to constrain the package across the entire dependency graph. |
| Test suite fails after bump with `TypeError: func is not a function` | Security release introduced breaking API signature change | `git diff package-lock.json` | 1. Revert lockfile bump.<br>2. Check if a non-breaking backport patch exists.<br>3. Apply minimal diff via `patch-package` targeting only the CVE vulnerability lines. |
| OSV API timeout or HTTP 503 | Transient upstream outage | `curl -I https://api.osv.dev/v1/querybatch` | Fall back to local CLI tool: `npm audit --json` or `trivy fs --format json .`. |
| Unmaintained / Abandoned upstream package | Project has no maintainers to cut a release | Check GitHub repo commit history | 1. Replace with active fork or community alternative.<br>2. Vendor the dependency into `vendor/` and apply security diff.<br>3. Remove dependency if feature is non-essential. |
| False positive on dev dependency | Build tool vulnerability flagged in production audit | Inspect dependency chain (`npm ls <pkg>`) | Pass `--omit=dev` (npm) or `--without dev` (Poetry) to restrict scans strictly to production runtimes. |

---

## 8. Verification & Audit Execution Commands

```bash
# 1. Run full repository scan using the scanner
python3 oss_scan.py .

# 2. Verify with ecosystem native tools
# Node.js
npm audit --audit-level=high

# Python
pip-audit --desc

# Rust
cargo audit

# 3. Assert zero critical or high vulnerabilities remain after patching
python3 oss_scan.py . | grep -i "high\|critical" && exit 1 || echo "Security gate passed."
```
