---
type: Playbook
id: https://w3id.org/lmodel/collections/knowledge/playbooks/release
genre: how-to
title: Release
description: "How a release is made: write `## [Unreleased]` in CHANGELOG.md, merge a `feat:`, `fix:` or `security:` change, and semantic-release tags it from the `v0.0.0` baseline, the first release being 0.1.0, after which Knowledge Release attaches the schema copy and the bundle."
resource: .releaserc.json
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - id: releaserc.json
    resource: .releaserc.json
    title: the release rules and the plugins
  - id: changelog.md
    resource: CHANGELOG.md
    title: the baseline paragraph
  - resource: .github/scripts/changelog-release.mjs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Release

1. Write each change under `## [Unreleased]` in CHANGELOG.md; the release job refuses an empty one.[^contributing.md]
2. Merge a change typed `feat:`, `fix:` or `security:`, or one marked breaking. Other types wait for the next release.
3. On the push to `main`, `semantic-release.yml` retitles the section, commits CHANGELOG.md and tags `vX.Y.Z`.

`.releaserc.json` maps a breaking change to a minor release and `security` to a patch.[^releaserc.json] The `v0.0.0` tag on `main` is the baseline, so the first release is 0.1.0.[^changelog.md] Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, the job dispatches Knowledge Release, which attaches `schema-<tag>-collections.yaml`, the bundle and a Copilot skill zip.

[^contributing.md]: CONTRIBUTING.md, Releasing (maintainers)
[^releaserc.json]: .releaserc.json, the release rules
[^changelog.md]: CHANGELOG.md, the baseline paragraph
