---
type: GlossaryTerm
id: https://w3id.org/lmodel/collections/knowledge/glossary/list
genre: reference
title: List
description: "A list in the Collections Ontology (`coll:List`): a bag whose items are in order, each with its place from 1, a first and a last item, and links to the items before and after it."
resource: src/collections/schema/collections.yaml
definedBy:
  - http://purl.org/co/List
  - https://w3id.org/lmodel/collections/knowledge/datasets/collections-linkml-schema
sources:
  - id: schema-collections.yaml
    resource: src/collections/schema/collections.yaml
    title: List, ListItem and their slots
generated:
  by: process:ktl-librarian
  at: "2026-11-01T00:01:52Z"
status: draft
references:
  - https://w3id.org/lmodel/collections/knowledge/glossary/bag
  - https://w3id.org/lmodel/collections/knowledge/glossary/item
---

# List

A **list** is a [bag](bag.md) whose items are list items, each with its place in `co_index`, counting from 1. A list may name its `firstItem` and `lastItem`. A list item may name its `nextItem` and `previousItem`, and the items after and before it in `followedBy` and `precededBy`. The schema renders the list as `List`, with the IRI `coll:List`, and the list item as `ListItem`, a kind of [item](item.md).[^schema-collections.yaml]

Items have no IRI in this schema, so each link holds a copy of the item it names. The tests check that the indexes count from 1 with no gap and that every link agrees with them.

`followedBy` and `precededBy` name `nextItem` and `previousItem` as their transitive form. The schema maps the list and the list item to schema.org's `ItemList` and `ListItem`, which link list items the same way.[^schema-collections.yaml]

[^schema-collections.yaml]: src/collections/schema/collections.yaml, List, ListItem and their slots
