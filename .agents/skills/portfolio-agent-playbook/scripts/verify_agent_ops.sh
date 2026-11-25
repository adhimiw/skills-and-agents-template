#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(pwd)}"
cd "$ROOT"

echo "==> Running unit/security/agent backend tests"
npm test

echo "==> Running strict realtime OAuth + Mistral + AI Agent verification"
npm run devops:verify:live
