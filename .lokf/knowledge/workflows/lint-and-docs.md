---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/workflows/lint-and-docs
genre: reference
title: Lint & docs (lint-and-docs.yaml)
description: "The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, Mondays at 06:00 UTC and by hand, it runs ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell."
resource: .github/workflows/lint-and-docs.yaml
sources:
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
    title: the header comment and the four jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Lint & docs (lint-and-docs.yaml)

`.github/workflows/lint-and-docs.yaml` checks the shell, the workflows and the prose. Its four read-only jobs run ShellCheck, actionlint, the word budgets (1000 for CONTRIBUTING.md, 900 for SECURITY.md), and markdownlint, lychee and codespell over the Markdown files.[^lint-and-docs.yaml] It runs on a push to `main`, on every pull request, on Mondays at 06:00 UTC to catch link rot, and by hand.

[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml, the header comment and the four jobs
