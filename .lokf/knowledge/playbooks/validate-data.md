---
type: Playbook
id: https://w3id.org/lmodel/collections/knowledge/playbooks/validate-data
genre: how-to
title: Validate data
description: How to check a collection, set, bag or list file against the schema with `linkml-validate`, and which of CO's rules only `tests/test_data.py` checks.
resource: docs/index.md
sources:
  - id: index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Validate data

Run `linkml-validate -s src/collections/schema/collections.yaml -C List list.yaml`, with the class the file holds after `-C`. It checks the file against the JSON Schema generated from the schema.[^index.md]

The validator does not check that a set repeats no element, that a size is the count, or that a list's indexes and links agree. `rule_faults` in `tests/test_data.py` checks them; [Scope and rules](../explanations/scope-and-rules.md) lists them.

[^index.md]: docs/index.md, the Validating data section
