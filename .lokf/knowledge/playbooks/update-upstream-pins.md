---
type: Playbook
id: https://w3id.org/lmodel/collections/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the upstream watch reports a new commit on CO's master branch, a changed or dropped `collections.owl`, another edition in `owl:versionInfo`, or a licence: replace the copy, move the pins in `scripts/check_upstream_release.py` and the schema header together, and run the tests."
resource: scripts/check_upstream_release.py
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring and the pins
  - id: report-issue.sh
    resource: .github/scripts/report-issue.sh
    title: the header comment
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Update the upstream pins

`scripts/check_upstream_release.py` pins CO's branch, `master`, the commit `619e7b0`, the edition `2.0`, the file `collections.owl` and its git object. It exits 1 when the branch moves, the file changes or goes, the copy drifts, the edition moves, a licence appears, or a check cannot finish.[^check_upstream_release.py] `.github/scripts/report-issue.sh` then opens one issue, or comments on the open one.[^report-issue.sh]

1. Read what changed at the new commit.
2. Replace `src/collections/schema/upstream/collections.owl` with the file at that commit.
3. Move `PINNED_COMMIT`, `PINNED_BLOB` and, for a new edition, `PINNED_EDITION`, with the schema header's `version` and annotations.
4. Update the schema, run the gate, and update NOTICE for a licence.

`tests/test_upstream.py` holds the header and the pins equal.

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring and the pins
[^report-issue.sh]: .github/scripts/report-issue.sh, the header comment
