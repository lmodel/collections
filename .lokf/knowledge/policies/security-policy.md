---
type: Policy
id: https://w3id.org/lmodel/collections/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
    title: every section
  - id: dependabot.yml
    resource: .github/dependabot.yml
    title: the six update entries
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:10:16Z"
status: draft
---

# Security policy

`SECURITY.md` asks for a vulnerability to be reported through GitHub's private vulnerability reporting, not in a public issue. One person maintains the repository, so a first reply takes days and there is no bounty. Only the latest release receives fixes.[^security.md]

A release attaches the adapt copy, the bundle as a zip and a Microsoft 365 Copilot skill zip, each with its `.sha256` and a build-provenance attestation. Nothing is published to PyPI. The upstream watch reads CO's GitHub repository and follows a redirect only to GitHub. It sends the job's token, which can also write issues, to `api.github.com` alone, and writes nothing but its report.

The policy's table names each workflow and what holds it:

- read-only pull request checks;
- a release job only on a push to `main`, in the `release` Environment;
- the Pages scopes on the website's deploy job alone;
- a librarian whose agent holds no write token.

Every workflow pins its actions to commit hashes, and Dependabot keeps them and the two uv locks and two npm locks current, each monthly.[^dependabot.yml]

A ruleset named `main` on the default branch blocks deletion and force-pushes and requires a linear history. Two settings are not yet in force: required reviewers on the `release` Environment, and secret scanning with push protection.

[^security.md]: SECURITY.md, every section
[^dependabot.yml]: .github/dependabot.yml, the six entries
