---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: "The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`."
resource: .github/workflows/main.yaml
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the on key and the test job
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Build and test (main.yaml)

`.github/workflows/main.yaml` runs on a push to `main` and on every pull request, with `contents: read`. Its `test` job installs `just` 1.47.0 and the project with `uv sync --locked --group dev`, and runs `just test` on Python 3.10 to 3.14. On Python 3.13 it also runs `just lint` and `just lokf-adapt-check`, which fails when `.lokf/collections.yaml` is stale.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml, the on key and the test job
