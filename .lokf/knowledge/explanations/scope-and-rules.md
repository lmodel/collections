---
type: Explanation
id: https://w3id.org/lmodel/collections/knowledge/explanations/scope-and-rules
genre: explanation
title: Scope and rules
description: What the schema renders of CO and leaves out, why a link to an item holds a copy of it, why it names no mapping, and the rules of CO that no validator checks, which the tests check over the examples instead.
resource: docs/index.md
sources:
  - id: index.md
    resource: docs/index.md
    title: the Validating data section
  - id: about.md
    resource: docs/about.md
    title: What is left out
  - id: readme.md
    resource: README.md
    title: the What it models, Influences, Mappings and Not modelled here sections
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Scope and rules

The schema renders every class and property of CO 2.0 and states the constraints LinkML can: an item wraps one element, a list item has an index from 1, a size is never below 0, and every class is closed. Items have no IRI, so a link to an item holds a copy of it. In RDF each copy is then a node of its own, where CO's own examples link to one named item.[^index.md]

No validator checks the rest of CO's rules, so `tests/test_data.py` checks them over the examples:

- a set holds no element twice;
- a size, where it is given, is the number of a set's elements or of a bag's or a list's items;
- an item's content is one of its bag's elements, where they are given;
- a list's indexes count from 1 with no gap or repeat, and `firstItem`, `lastItem` and each item's links agree with them.

The schema leaves out CO's property chains, SWRL rules and narrower-property axioms, CO's alignments with other vocabularies, and its example files.[^about.md] It names no mapping: CO's alignments name older vocabularies, and CO states none to RDF's containers.[^readme.md]

[^index.md]: docs/index.md, the Validating data section
[^about.md]: docs/about.md, What is left out
[^readme.md]: README.md, the What it models, Influences, Mappings and Not modelled here sections
