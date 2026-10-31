---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge Release (knowledge-release.yaml)
description: "The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: on a published release once `KNOWLEDGE_RELEASE_ENABLED` is `true`, or by hand for a tag, it attaches the schema copy, the bundle zip and the Copilot skill zip, each with its checksum and attestation."
resource: .github/workflows/knowledge-release.yaml
sources:
  - id: knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
    title: the pack and attach jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Knowledge Release (knowledge-release.yaml)

`.github/workflows/knowledge-release.yaml` runs on a published release, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, and by hand with a tag. Its `pack` job builds the assets with `contents: read` and skips a release whose bundle and domain schema are unchanged since the last release that carries a bundle. Its `attach` job holds `contents: write`, `id-token: write` and `attestations: write`, and attaches each asset with its `.sha256` and a build-provenance attestation.[^knowledge-release.yaml]

[^knowledge-release.yaml]: .github/workflows/knowledge-release.yaml, the pack and attach jobs
