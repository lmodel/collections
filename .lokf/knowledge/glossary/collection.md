---
type: GlossaryTerm
id: https://w3id.org/lmodel/collections/knowledge/glossary/collection
genre: reference
title: Collection
description: "A collection in the Collections Ontology (`coll:Collection`): a group of things taken as a whole, with its elements and its size; a set holds each element once, and a bag may hold one more than once."
resource: src/collections/schema/collections.yaml
definedBy:
  - http://purl.org/co/Collection
  - https://w3id.org/lmodel/collections/knowledge/datasets/collections-linkml-schema
sources:
  - id: schema-collections.yaml
    resource: src/collections/schema/collections.yaml
    title: Collection, Set and co_size
generated:
  by: process:ktl-librarian
  at: "2026-11-01T00:01:52Z"
status: draft
references:
  - https://w3id.org/lmodel/collections/knowledge/glossary/element
  - https://w3id.org/lmodel/collections/knowledge/glossary/bag
  - https://w3id.org/lmodel/collections/knowledge/glossary/item
---

# Collection

A **collection** is a group of things taken as a whole. Its things are its elements, in `element`, and each is an [element](element.md), named by its IRI. `co_size` counts how many times the collection holds a thing. The schema renders it as `Collection`, with the IRI `coll:Collection`.[^schema-collections.yaml]

A **set** (`coll:Set`) holds each element once, so its size is the number of its elements. A [bag](bag.md) may hold an element more than once. A set and a bag are disjoint, and a collection is never an [item](item.md).

CO's alignment file names the collection of SWAN Collections 1.2 and of the ontologydesignpatterns.org Collection Entity pattern as the same class, and ORE's aggregation as a narrower one.[^schema-collections.yaml]

[^schema-collections.yaml]: src/collections/schema/collections.yaml, Collection, Set and co_size
