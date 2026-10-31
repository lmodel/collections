---
type: GlossaryTerm
id: https://w3id.org/lmodel/collections/knowledge/glossary/item
genre: reference
title: Item
description: "An item in the Collections Ontology (`coll:Item`, the schema's `CoItem`): an entry of a bag that wraps one of the bag's elements in `itemContent`."
resource: src/collections/schema/collections.yaml
definedBy:
  - http://purl.org/co/Item
sources:
  - id: schema-collections.yaml
    resource: src/collections/schema/collections.yaml
    title: CoItem and itemContent
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Item

An **item** is an entry of a [bag](bag.md). It wraps one of the bag's elements, named by its IRI in `itemContent`, which every item requires. Two items of one bag may wrap the same element. The schema renders CO's `Item` as `CoItem`, with the IRI `coll:Item`, because UCO defines an `Item` of its own.[^schema-collections.yaml] A list's items are list items, which also have a place.

[^schema-collections.yaml]: src/collections/schema/collections.yaml, CoItem and itemContent
