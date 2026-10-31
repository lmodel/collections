---
type: Playbook
id: https://w3id.org/lmodel/collections/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: "How to change the schema: install with `uv sync --group dev`, edit `src/collections/schema/collections.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit the regenerated files."
resource: CONTRIBUTING.md
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Development setup and Before opening a pull request
  - id: justfile
    resource: justfile
    title: the lint, gen-project, gen-doc and test recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Regenerate and test

1. Install the tools: Python 3.10 or later, uv and just, then `uv sync --group dev`.[^contributing.md]
2. Edit `src/collections/schema/collections.yaml`, keeping CO's names and IRIs.
3. Run `just lint`, which fails on a warning under `.linkmllint.yaml`.[^justfile]
4. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit what they write.
5. Run `just test`: it generates the project into `tmp/`, runs pytest and runs the examples.
6. Run `uvx pre-commit run` on what you staged.

A change to `.lokf/` also needs `cd .lokf && just lokf-validate`.

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the lint, gen-project, gen-doc and test recipes
