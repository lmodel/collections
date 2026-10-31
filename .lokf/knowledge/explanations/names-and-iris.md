---
type: Explanation
id: https://w3id.org/lmodel/collections/knowledge/explanations/names-and-iris
genre: explanation
title: Names and IRIs
description: Why the schema keeps CO's names and IRIs under the `coll` prefix, why `CoItem`, `co_size` and `co_index` differ from CO's names, how the terms match lmodel/uco's `uco_co` module, and the one key, `element`, the adapt copy shares with spdx's.
resource: docs/about.md
sources:
  - id: about.md
    resource: docs/about.md
    title: the naming paragraph
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: schema-collections.yaml
    resource: src/collections/schema/collections.yaml
    title: the header notes
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the shared key
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:19:29Z"
status: draft
---

# Names and IRIs

The schema renders an ontology, so it keeps the ontology's names and IRIs: data written against it uses CO's property names as its keys, and every class and slot projects under CO's own IRI. The prefix is `coll`, which LinkML's prefix map gives CO's namespace. The same map gives `co` to another vocabulary.[^about.md]

Three names differ, each with CO's IRI kept:

- `CoItem` for CO's `Item` and `co_size` for its `size`, as lmodel/uco's `uco_co` module names them, because UCO defines an `Item` and a `size` of its own.
- `co_index` for CO's `index`, because LinkML's documentation generator writes the page of a slot named `index` over the schema's index page.[^schema-collections.yaml]

The README says that `uco_co` renders the CO terms UCO uses with the same IRIs and the same names but one: `index`, which is `co_index` here. So a host imports one of the two copies, not both.[^readme.md] A host that imports this copy beside spdx's has one key under two IRIs: `element`, which spdx uses for an SPDX element's members. `tests/test_schema_rules.py` lists that key and fails on a new one.[^test_schema_rules.py]

[^about.md]: docs/about.md, the naming paragraph
[^schema-collections.yaml]: src/collections/schema/collections.yaml, the header notes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, the shared key
