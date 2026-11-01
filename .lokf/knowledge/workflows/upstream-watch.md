---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its co-copy job runs `scripts/check_upstream_release.py` against CO's GitHub repository, and on a finding opens or updates the issue titled Upstream watch: the Collections Ontology has changed."
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the on key and the job
generated:
  by: process:ktl-librarian
  at: "2026-11-01T00:02:57Z"
status: draft
references:
  - https://w3id.org/lmodel/collections/knowledge/playbooks/update-upstream-pins
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` runs every Monday at 07:00 UTC and by hand. Its one job, `co-copy`, reads the checkout and holds `issues: write`. It runs `scripts/check_upstream_release.py` with the workflow's token, which raises GitHub's rate limit. On a finding, `.github/scripts/report-issue.sh` opens the issue titled "Upstream watch: the Collections Ontology has changed" or comments on the open one.[^upstream-watch.yaml] [Update the upstream pins](../playbooks/update-upstream-pins.md) says what each finding asks for.

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the on key and the job
