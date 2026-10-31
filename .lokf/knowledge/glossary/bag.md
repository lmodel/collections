---
type: GlossaryTerm
id: https://w3id.org/lmodel/collections/knowledge/glossary/bag
genre: reference
title: Bag
description: "A bag in the Collections Ontology (`coll:Bag`): a collection that may hold one element more than once, in no order, through items that each wrap one element."
resource: src/collections/schema/collections.yaml
definedBy:
  - http://purl.org/co/Bag
sources:
  - id: schema-collections.yaml
    resource: src/collections/schema/collections.yaml
    title: Bag and item
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Bag

A **bag** is a [collection](collection.md) that may hold one element more than once, in no order. It holds them through its items, in `item`: each [item](item.md) wraps one element. Its size is the number of its items, so a bag holding `a` twice and `b` once has the size 3. The schema renders it as `Bag`, with the IRI `coll:Bag`.[^schema-collections.yaml] A [list](list.md) is a bag whose items are in order.

[^schema-collections.yaml]: src/collections/schema/collections.yaml, Bag and item
