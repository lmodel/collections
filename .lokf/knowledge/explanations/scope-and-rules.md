---
type: Explanation
id: https://w3id.org/lmodel/collections/knowledge/explanations/scope-and-rules
genre: explanation
title: Scope and rules
description: What the schema renders of CO, adds to it (`CoElement`) and leaves out, why a link to an item holds a copy of it, where its mappings come from, and the rules of CO that no validator checks, which the tests check over the examples instead.
resource: docs/index.md
sources:
  - id: index.md
    resource: docs/index.md
    title: the Validating data section
  - id: about.md
    resource: docs/about.md
    title: the paragraph on CoElement and What is left out
  - id: readme.md
    resource: README.md
    title: the What it models, Influences, Mappings and Not modelled here sections
generated:
  by: process:ktl-librarian
  at: "2026-11-01T00:10:55Z"
status: draft
---

# Scope and rules

The schema renders every class and property of CO 2.0 and states the constraints LinkML can: an item wraps one element, a list item has an index from 1, a size is never below 0, and every class is closed. Items have no IRI, so a link to an item holds a copy of it. In RDF each copy is then a node of its own, where CO's own examples link to one named item.[^index.md]

The schema adds one class, `CoElement`, so that in RDF a collection links to its elements as resources rather than holding their IRIs as text.[^about.md]

No validator checks the rest of CO's rules, so `tests/test_data.py` checks them over the examples:

- a set holds no element twice;
- a size, where it is given, is the number of a set's elements or of a bag's or a list's items;
- an item's content is one of its bag's elements, where they are given;
- a list's indexes count from 1 with no gap or repeat, and `firstItem`, `lastItem` and each item's links agree with them.

The schema leaves out CO's SWRL rules and the narrower-property axioms on single-valued slots, such as `firstItem` under `item`. LinkML's inheritance is monotonic, so a slot under a multivalued parent is multivalued too. It states CO's two property chains as path rules, which no generator reads. It also leaves out CO's example files.[^about.md]

The exact, narrow and broad mappings come from CO's own alignment file, and the mappings to schema.org are the project's own. CO states no mapping to RDF's containers, so the schema names none.[^readme.md]

[^index.md]: docs/index.md, the Validating data section
[^about.md]: docs/about.md, the paragraph on CoElement and What is left out
[^readme.md]: README.md, the What it models, Influences, Mappings and Not modelled here sections
