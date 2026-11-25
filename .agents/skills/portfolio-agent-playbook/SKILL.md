---
name: portfolio-agent-playbook
description: Operational playbook for connecting GitHub and LinkedIn OAuth locally into the AES-256-GCM MongoDB Env Vault via browser automation (chrome-mcp), running and verifying the Mistral AI Research & Publishing Agent, executing the 7-stage realtime DevOps pipeline, and diagnosing Inference Engineering telemetry or rate-limit cascades. Use when onboarding local OAuth credentials, testing or debugging the AI Agent across GitHub/LinkedIn, or verifying live DevOps integration readiness.
---

# Portfolio Agent & OAuth Ops Playbook

Runbook for operating the Mistral AI Research & Publishing Agent, local OAuth credential lifecycle, and realtime DevOps verification in `lab-portfolio`.

## 1. Local OAuth Bootstrap via `chrome-mcp`

Never store third-party credentials in `.env` or git. Authenticate once in the user's Chrome session via `chrome-mcp` so the backend persists tokens AES-256-GCM encrypted inside MongoDB `VaultSecret`:

1. Start local stack (`npm run dev` on `:3000` web / `:4000` API + MongoDB on `127.0.0.1:27017`).
2. Confirm `FRONTEND_URL` in MongoDB Vault matches the browser origin (`http://localhost:3000`) and both `GITHUB_CLIENT_ID`/`SECRET` and `LINKEDIN_CLIENT_ID`/`SECRET` are set in **Env Vault (DB)**.
3. **GitHub OAuth**:
   - Open `/admin` in an unused Chrome tab (`chrome_navigate`), click **Sign in with GitHub OAuth (`adhimiw`)**.
   - Confirm callback returns to `/admin?connected=github`, setting the signed `HttpOnly` cookie and refreshing `GITHUB_OAUTH_TOKEN` (`read:user, repo` scopes) in Vault.
4. **LinkedIn OAuth**:
   - Navigate to **LinkedIn Showcase** (`?tab=linkedin`) and click **Connect LinkedIn OAuth** (`/api/auth/linkedin` requires active admin session).
   - Complete LinkedIn sign-in/consent in the live Chrome tab if prompted (`LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_PERSON_URN`, `LINKEDIN_MEMBER_NAME` save encrypted in Vault).

## 2. Executing & Verifying the Mistral AI Agent

Operate the agent from `/admin?tab=agent` (**AI Agent**) or `POST /api/agent/command`:

- **GitHub Deep Import**: `"Add https://github.com/<owner>/<repo> to <capstone|freelancing|hobbie>"` (use `mode: "preview"` first when testing without mutating live data). Inspects metadata, `README.md`, recursive Git tree, manifests, `.github/workflows/*.yml`, and Zip-Slip-safe Action artifacts; downloads magic-byte-verified raster images to `/uploads/projects/`.
- **LinkedIn Publish & Curate**:
  - Publish copy directly or pass URL + optional `linkedinText` / uploaded raster image when LinkedIn returns an HTTP `999` login wall.
  - Set `"Sync & feature LinkedIn posts"` to sync `/rest/posts` (using active dynamic `YYYYMM` `LinkedIn-Version`, handling `403 ACCESS_DENIED` when `r_member_social` is unapproved) and toggle `featuredOnSite`.
- **Live Frontend Sync**: Every mutation bumps `GET /api/portfolio/version` and broadcasts `adhithan_portfolio_sync`, refreshing open `/` tabs without reload.

## 3. Inference Engineering & Failure Recovery

- **Model Cascade**: Defaults to `ministral-14b-latest` -> `codestral-latest` -> `ministral-8b-latest` -> `ministral-3b-latest` -> deterministic README/manifest fallback.
- **Zero-RPM `429` Handling**: Any model returning `x-ratelimit-limit-req-minute: "0"` trips its in-memory circuit breaker (`300s` cooldown) and cascades immediately; rotating `MISTRAL_API_KEY` or `MISTRAL_MODEL` in Vault resets circuits cleanly (`clearMistralCircuits()`).
- **Observability**: Inspect **Inference Engineering Observability** in **AI Agent** or `GET /api/agent/metrics` for `P50`/`P90`/`P95`/`P99` latency, KV prefix `cacheHitRatePct`, and `2XX`/`429`/`4XX`/`5XX` counters.

## 4. Realtime DevOps Verification Gates

- Run strict live integration probe (GitHub OAuth + LinkedIn `/v2/userinfo` & active REST header + Mistral + AI Agent preview):
  ```bash
  npm run devops:verify:live
  ```
- Run the full 7-stage local pipeline (Security Hygiene -> Contrast/Parity -> 35 Unit/Integration/Security Tests -> Dual React + Play Store Leakage Scan -> Production Smoke -> Playwright 9-Tab E2E -> Realtime Live Probe):
  ```bash
  npm run pipeline
  ```
- Sync updated skills & release state to private GitHub repositories:
  ```bash
  npm run skills:sync
  ```

## Detailed Technical Matrix

Read [references/oauth-and-mistral-matrix.md](references/oauth-and-mistral-matrix.md) when inspecting OAuth callback URIs, active LinkedIn API version rules, Mistral model tier quotas, or applied arXiv hardening citations, or execute `scripts/verify_agent_ops.sh` to validate live readiness.
