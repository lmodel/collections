---
type: GlossaryTerm
id: https://w3id.org/lmodel/collections/knowledge/glossary/collection
genre: reference
title: Collection
description: "A collection in the Collections Ontology (`coll:Collection`): a group of things taken as a whole, with its elements and its size; a set holds each element once, and a bag may hold one more than once."
resource: src/collections/schema/collections.yaml
definedBy:
  - http://purl.org/co/Collection
sources:
  - id: schema-collections.yaml
    resource: src/collections/schema/collections.yaml
    title: Collection, Set and co_size
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Collection

A **collection** is a group of things taken as a whole. Its things are its elements, in `element`, each named by its IRI, and `co_size` counts how many times it holds a thing. The schema renders it as `Collection`, with the IRI `coll:Collection`.[^schema-collections.yaml]

A **set** (`coll:Set`) holds each element once, so its size is the number of its elements. A [bag](bag.md) may hold an element more than once. A set and a bag are disjoint, and a collection is never an [item](item.md).

[^schema-collections.yaml]: src/collections/schema/collections.yaml, Collection, Set and co_size
