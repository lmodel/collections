---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge Librarian (knowledge-librarian.yaml)
description: "The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: Mondays at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`, it runs the ktl-librarian skill pinned to KTL v0.59.0 in a job with no write token and opens a pull request with what changed."
resource: .github/workflows/knowledge-librarian.yaml
sources:
  - id: knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
    title: the skills pin and the earlier, refresh and publish jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-01T00:01:52Z"
---

# Knowledge Librarian (knowledge-librarian.yaml)

`.github/workflows/knowledge-librarian.yaml` pins the skills to `TRUST_LADDER_SKILLS_REF` v0.59.0. The `earlier` job finds an open librarian pull request. The `refresh` job runs the agent in the `knowledge-librarian` Environment with `contents: read`, once `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`. The `publish` job, which runs no agent, applies the agent's patch and opens the pull request.[^knowledge-librarian.yaml]

[^knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml, the skills pin and the earlier, refresh and publish jobs
