---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: "The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: Mondays at 04:10 UTC and by hand, it compares the sidecar's copies and the skills pin with the newest KTL release and opens one pull request when they are behind."
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the earlier, sync, publish, review and push-workflows jobs
  - resource: .github/PULL_REQUEST_TEMPLATE
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-01T00:01:52Z"
---

# Knowledge sync (knowledge-sync.yaml)

`.github/workflows/knowledge-sync.yaml` keeps the copies `knowledge-sync.manifest` lists at the newest KTL release. Its `sync` job writes the new copies with `contents: read`. Its `publish` job runs in the `knowledge-sync` Environment and opens the pull request from `.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md`. A change to a workflow waits in `review`, in the Environment `KNOWLEDGE_SYNC_REVIEW_ENVIRONMENT` names.[^knowledge-sync.yaml]

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the earlier, sync, publish, review and push-workflows jobs
