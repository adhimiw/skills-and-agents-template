---
name: portfolio-master
description: >-
  Primary self-updating engineering skill for Adhithan's React 19 + MongoDB
  portfolio, mobile PWA resume app, encrypted DB Env Vault, GitHub/LinkedIn
  integrations, and local DevOps pipeline. Use when building features, running
  the CI/CD pipeline, adding integrations, or syncing updated skills and code
  to private GitHub repositories.
---

# portfolio-master

Core architectural contract and self-updating skill for `lab-portfolio` and
`skills-and-agents-template`.

## Architectural Invariants

1. **Design System**: Warm paper `#EEEAE1`, dense ink `#24221E`, electric cobalt `#2535D9`.
   Fonts: `Pixelify Sans` (display wordmark/name), `Host Grotesk Variable` (body/headings),
   `JetBrains Mono Variable` (code/metadata). Zero fake metrics or glassmorphism.
2. **Hero Spotlight**: `src/lib/dither.js` renders Adhithan's original portrait in halftone dots
   and reveals the full-color photo strictly inside the circular pointer hover spotlight.
3. **Encrypted DB Env Vault**: Store third-party tokens and OAuth secrets AES-256-GCM encrypted
   in MongoDB (`VaultSecret` via `server/services/vault.js`). Never commit `.env` or `.data/vault.key`.
4. **Auth & Integrations**:
   - GitHub OAuth / PAT verified against `ALLOWED_GITHUB_LOGIN` (`adhimiw`), issuing `HttpOnly` session cookies.
   - Projects categorized under `capstone`, `freelancing`, and `hobbie` with backend sorting.
   - LinkedIn posts controlled by explicit `featuredOnSite` toggle (`PATCH /api/linkedin/posts/:id/toggle`).
   - Resume available as mobile PWA (`/resume`) and validated PDF upload (`/api/resume/upload`).

## Workflows

- **Verify before shipping**: Run `npm run pipeline` (security hygiene, WCAG contrast, parity, API tests, React build, smoke probe).
- **Read current live state**: See `references/project-state.md` (auto-updated by script).
- **Self-update skill & sync to GitHub**: Run `npm run skills:sync` (or `bash .agents/skills/portfolio-master/scripts/update-and-sync.sh`).
  This refreshes `references/project-state.md` from live models/routes/versions, mirrors updated skills to
  `/home/adhithan/Projects/skills-and-agents-template/.agents/skills/`, and pushes committed changes to private GitHub remotes.
