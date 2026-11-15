---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: "The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request its plan job says what a merge would release, and on a push to main its release job, in the release Environment, tags the release and dispatches Knowledge Release."
resource: .github/workflows/semantic-release.yml
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the plan and release jobs
  - id: package.json
    resource: .release/package.json
    title: the release tools
  - resource: .release
generated:
  by: process:ktl-librarian
  at: "2026-11-15T20:56:10Z"
status: draft
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` has two jobs. On a pull request into `main`, `plan` previews what a merge would release, with `--dry-run`, and needs no write scope. On a push to `main`, `release` runs in the `release` Environment with `contents: write` and `actions: write`, promotes CHANGELOG.md, tags the release, and dispatches Knowledge Release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.[^semantic-release.yml] Both install semantic-release from `.release/package-lock.json` with `npm ci --ignore-scripts`.[^package.json]

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the plan and release jobs
[^package.json]: .release/package.json, the release tools
