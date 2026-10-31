---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: it builds the site on pull requests and pushes that touch its inputs, Mondays at 05:23 UTC and by hand, and deploys it to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`."
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the build and deploy jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` comes from the ktl-website templates. Its `build` job builds `website/` with `contents: read`. Its `deploy` job holds `pages: write` and `id-token: write`, runs in the `github-pages` Environment, and deploys only once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`.[^knowledge-website.yaml] [The documentation website](../services/documentation-site.md) says what the site shows.

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the build and deploy jobs
