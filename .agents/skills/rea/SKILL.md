---
name: rea
description: Reverse Engineer Anything (REA) analysis engine based on morluto/rea. Use when analyzing compiled binaries, disassembling native code, decompiling Android APKs, inspecting Web/Electron bundles, examining .NET assemblies, and performing evidence-based reverse engineering.
allowed-tools: Read Write Edit Glob Grep
---

# REA: Reverse Engineer Anything Analysis Engine

## Overview

`rea` equips AI agents with deep reverse engineering, binary analysis, and runtime inspection capabilities without requiring original source code. Based on `morluto/rea`, this skill provides structured protocols for decompilation, disassembly, network traffic reconstruction, and clean-room reimplementation following the **Seen / Inferred / Unknown** evidence ledger.

---

## Triggers & Activation Scenarios

Activate this skill when:
- Inspecting native Linux/Windows/macOS binaries (ELF, PE, Mach-O) for functions, strings, and symbols.
- Decompiling Android APKs / DEX files (Apktool, Jadx, ADB inspection).
- Unpacking Electron applications, obfuscated JavaScript bundles, or WebAssembly modules.
- Analyzing proprietary network protocols or captured PCAP streams.
- Performing clean-room reimplementation of proprietary APIs or software behaviors.

---

## 1. Evidence-Based Epistemology

All conclusions drawn by REA must be categorized strictly:
* **Seen (Facts):** Direct disassembly, decompiled lines, strings, HTTP headers, or register values with file/offset citations.
* **Inferred (Hypotheses):** Logical algorithms or state flows deduced from seen data; requires experimental validation.
* **Unknown (Gaps):** Unresolved symbols, stripped function pointers, encrypted payloads, or missing branches.

---

## 2. MCP Tools & Commands

REA provides an extensive suite of over 100 specialized MCP tools:

### Native Binary Inspection
```bash
# Analyze binary layout, architectures, and compiler signatures
rea inspect binary --file ./target_binary

# Decompile specific procedure or entrypoint
rea decompile --address 0x00401000
```

### Android APK Analysis
```bash
# Decompile and unpack APK manifest, activities, and permissions
rea inspect apk --path ./app-release.apk

# Search for embedded API keys or endpoints in DEX strings
rea apk search-strings --pattern "https?://"
```

### Web & Electron Inspection
```bash
# Extract and format packed app.asar archive
rea inspect electron --path /path/to/resources/app.asar
```

---

## 3. Clean-Room Reimplementation Protocol

```
+--------------------+        Evidence Extraction       +--------------------+
|  Compiled Target   |  =============================>  |  Ledger Document   |
| (Binary, APK, App) |                                  |  (Seen / Inferred) |
+--------------------+                                  +--------------------+
                                                                  ||
                                                                  || Specification
                                                                  \/
                                                        +--------------------+
                                                        | Clean-Room Source  |
                                                        | (Pure Re-creation) |
                                                        +--------------------+
```
1. **Extraction:** Gather public API signatures, serialized shapes, and protocol behaviors.
2. **Isolation:** Write an implementation specification containing zero proprietary binary code.
3. **Synthesis:** Build a modern, maintainable implementation in Rust, TypeScript, or Python.
