---
type: Dataset
id: https://w3id.org/lmodel/collections/knowledge/datasets/test-data
genre: reference
title: Tests and example data
description: "The tests under `tests/`: 10 valid examples, 11 counter-examples the validator rejects and 14 that break a rule only a test checks, the checks against CO's OWL file and the watch's stubbed answers, and the 13 released neighbour copies the adapt copy is held apart from."
resource: tests
sources:
  - id: test_data.py
    resource: tests/test_data.py
    title: the example tests and the rule checks
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the module docstring and the tests
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the neighbours, the shared key and the root
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the module docstring
  - resource: tests/data
  - resource: tests/neighbours
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Tests and example data

`tests/data/valid/` holds 10 examples, at least one per class, and `tests/data/invalid/` holds 11 counter-examples. Each counter-example's first line names, as `# Fails at:`, where the validator must reject it, and `tests/test_data.py` checks that it fails there and only there. It also holds every example to the committed `project/jsonschema/collections.schema.json`.[^test_data.py]

`tests/data/problem/invalid/` holds 14 counter-examples of the rules no validator checks, such as a set that repeats an element or a list whose indexes have a gap. Each passes the validator and breaks its rule at the place its first line names, which `rule_faults` in `tests/test_data.py` finds. The same check holds every valid example.

`tests/test_upstream.py` holds the schema to the copy of CO's OWL file and the header to the watch's pins.[^test_upstream.py] `tests/test_schema_rules.py` holds the adapt copy apart from LOKF and from 13 released lmodel copies in `tests/neighbours/`, each pinned by its checksum, and lists `element` as the one key shared with spdx's copy.[^test_schema_rules.py] `tests/test_watch.py` runs the watch against stubbed answers from GitHub.[^test_watch.py]

[^test_data.py]: tests/test_data.py, the example tests and the rule checks
[^test_upstream.py]: tests/test_upstream.py, the module docstring and the tests
[^test_schema_rules.py]: tests/test_schema_rules.py, the neighbours, the shared key and the root
[^test_watch.py]: tests/test_watch.py, the module docstring
