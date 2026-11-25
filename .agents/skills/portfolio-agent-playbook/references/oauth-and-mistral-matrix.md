# OAuth Endpoints, Mistral Quotas & Hardening Reference

## Contents
1. [OAuth Routes & Vault Keys](#1-oauth-routes--vault-keys)
2. [Mistral Model Tier Matrix](#2-mistral-model-tier-matrix)
3. [arXiv 2026 Hardening Patterns Applied](#3-arxiv-2026-hardening-patterns-applied)

---

## 1. OAuth Routes & Vault Keys

| Integration | Admin Start Route | Callback Route | Vault Secrets Populated | Notes |
|---|---|---|---|---|
| **GitHub OAuth** | `GET /api/auth/github` | `GET /api/auth/github/callback` | `GITHUB_OAUTH_TOKEN` | Enforces `ALLOWED_GITHUB_LOGIN`; `read:user repo` scope |
| **GitHub PAT** | `POST /api/auth/github-token` | — | `GITHUB_PAT` | Ideal for CLI/headless bearer setup; stale `401` falls back cleanly on public repos |
| **LinkedIn OAuth** | `GET /api/auth/linkedin` (`requireAdmin`) | `GET /api/auth/linkedin/callback` (`requireAdmin`) | `LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_PERSON_URN`, `LINKEDIN_MEMBER_NAME` | `/v2/userinfo` (`openid profile email`); `/rest/posts` requires dynamic `YYYYMM` `LinkedIn-Version` + `r_member_social` |
| **Mistral AI** | Vault UI (`category: ai`) | — | `MISTRAL_API_KEY`, `MISTRAL_MODEL`, `MISTRAL_FALLBACK_MODEL` | Rotating any Mistral Vault key calls `clearMistralCircuits()` |

---

## 2. Mistral Model Tier Matrix

Measured via live `/v1/chat/completions` & `x-ratelimit-*` probes:

| Model ID | Observed Status | Rate Limit Bucket | Features | Role |
|---|---|---|---|---|
| `ministral-14b-latest` | `200 OK` | `2 RPM` / `40,000 TPM` | `strict: true` JSON schema, `prompt_cache_key` | Default primary |
| `codestral-latest` | `200 OK` | `2 RPM` / `40,000 TPM` | `strict: true` JSON schema, `prompt_cache_key` | Cascade Tier 2 |
| `ministral-8b-latest` | `200 OK` | `2 RPM` / `40,000 TPM` | `strict: true` JSON schema, `prompt_cache_key` | Cascade Tier 3 |
| `ministral-3b-latest` | `200 OK` | `2 RPM` / `40,000 TPM` | `prompt_cache_key` | Cascade Tier 4 |
| `mistral-small-latest` | `429 (1300)` | `0 RPM` (`limit: 0`) | Auto-tripped (`300s`) | Cascaded past automatically |
| `mistral-medium-latest` | `429 (1300)` | `0 RPM` (`limit: 0`) | Auto-tripped (`300s`) | Cascaded past automatically |

---

## 3. arXiv 2026 Hardening Patterns Applied

Retrieved via `https://info.arxiv.org/help/api/index.html`:
- **Constrained Decoding & Zod Repair**: `2610.35328v1`, `2610.33949v1`, `2611.10977v1` (DM-Call cumulative diagnostic retries).
- **Minimal Candidate Tool Scoping & Backdoor Isolation**: `2610.23342v1`, `2611.00138v1` (Kerkoporta untrusted delimiter fences `<untrusted_repo_evidence>`).
- **Relational Integer Grounding & Pre-Mutation Gate**: `2611.02297v1` (FactorSpec `selectedImageIndices`), `2610.25552v1`, `2610.31840v2`.
- **Explicit Uncertainty & Budget Bounds**: `2611.23274v1` (`warnings[]`), `2611.12125v2`.
