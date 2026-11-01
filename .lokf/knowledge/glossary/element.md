---
type: GlossaryTerm
id: https://w3id.org/lmodel/collections/knowledge/glossary/element
genre: reference
title: Element
description: "An element in the schema (`CoElement`): a thing that a collection holds or an item wraps, named by its IRI, so that in RDF a collection links to its elements as resources; the one class that is not CO's."
resource: src/collections/schema/collections.yaml
definedBy:
  - https://w3id.org/lmodel/collections/knowledge/datasets/collections-linkml-schema
references:
  - https://w3id.org/lmodel/collections/knowledge/glossary/collection
  - https://w3id.org/lmodel/collections/knowledge/glossary/item
sources:
  - id: schema-collections.yaml
    resource: src/collections/schema/collections.yaml
    title: CoElement, element and itemContent
  - id: about.md
    resource: docs/about.md
    title: the paragraph on CoElement
generated:
  by: process:ktl-librarian
  at: "2026-11-01T00:01:52Z"
status: draft
---

# Element

An **element** is a thing that a [collection](collection.md) holds, in `element`, or that an [item](item.md) wraps, in `itemContent`. The schema renders it as `CoElement`, a class with one slot, `iri`, which names the thing and is its identifier. An element is never an item.[^schema-collections.yaml]

`CoElement` is the one class that is not CO's, so its IRI is the schema's own. CO lets `element` and `itemContent` hold anything. Because they range over `CoElement`, their values are links to resources in RDF and in the generated ontology, not text.[^about.md]

[^schema-collections.yaml]: src/collections/schema/collections.yaml, CoElement, element and itemContent
[^about.md]: docs/about.md, the paragraph on CoElement
