---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge Registrar (knowledge-registrar.yaml)
description: "The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the bundle's gate, which validates `.lokf/` on pull requests, Mondays at 06:00 UTC and by hand, and checks that each new confirmation is backed by its person's approval or signed commit."
resource: .github/workflows/knowledge-registrar.yaml
sources:
  - id: knowledge-registrar.yaml
    resource: .github/workflows/knowledge-registrar.yaml
    title: the validate, provenance and attestation jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Knowledge Registrar (knowledge-registrar.yaml)

`.github/workflows/knowledge-registrar.yaml` comes from the KTL v0.59.0 sidecar templates. Its `validate` job runs `just lokf-validate`, `just lokf-check-refs` and the conventions script. On a pull request, its `provenance` job checks each new confirmation against the pull request's approvals and signed commits. The `attestation` job, a fallback for a confirmation that neither backs, runs in the Environment `KNOWLEDGE_CURATION_ENVIRONMENT` names.[^knowledge-registrar.yaml]

[^knowledge-registrar.yaml]: .github/workflows/knowledge-registrar.yaml, the validate, provenance and attestation jobs
