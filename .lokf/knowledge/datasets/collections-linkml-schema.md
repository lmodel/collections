---
type: Dataset
id: https://w3id.org/lmodel/collections/knowledge/datasets/collections-linkml-schema
genre: reference
title: collections LinkML schema
description: "The LinkML schema of the Collections Ontology (CO) 2.0, `src/collections/schema/collections.yaml` (schema id `https://w3id.org/lmodel/collections`, version 2.0): six classes and sixteen slots, each with CO's name and IRI. Its `lokf adapt` copy `.lokf/collections.yaml`, rooted on `Collection`, is the bundle's domain schema."
resource: src/collections/schema/collections.yaml
version: "2.0"
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/collections/knowledge/references/collections-ontology
sources:
  - id: schema-collections.yaml
    resource: src/collections/schema/collections.yaml
    title: the header, the slots and the classes
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their root
  - id: lokf-collections.yaml
    resource: .lokf/collections.yaml
    title: the notes lokf adapt wrote
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the tool.lokf table
  - resource: .linkmllint.yaml
    title: the naming rule
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# collections LinkML schema

`src/collections/schema/collections.yaml` is the schema, titled "Collections Ontology (CO)". Its header gives `version: "2.0"`, CO's `owl:versionInfo`, and `source: https://github.com/collections-ontology/collections-ontology`. Its annotations name CO's ontology IRI, `http://purl.org/co`, the commit and the git object of the copied OWL file, and CO's licences as the Google Code archive gives them. The schema's own licence is Apache-2.0.[^schema-collections.yaml]

The schema binds `coll:` to CO's namespace, `http://purl.org/co/`, and gives every class a `class_uri` and every slot a `slot_uri` under it. It imports only `linkml:types`.

## Classes

- **`Collection`** holds `element` and `co_size`. **`Set`** and **`Bag`** are its subclasses, and **`List`** is a subclass of `Bag` with `firstItem` and `lastItem`.
- **`CoItem`** (CO's `Item`) is an entry of a bag and requires `itemContent`. **`ListItem`** is its subclass, which requires `co_index` and may hold `nextItem`, `previousItem`, `followedBy` and `precededBy`.

`Collection` and `CoItem` are disjoint, and so are `Bag` and `Set`. Items have no identifier, so a link to an item holds a copy of it. The schema states no mapping.

## Slots

Every slot keeps CO's local name, except `co_size` for CO's `size` and `co_index` for its `index`. `.linkmllint.yaml` lets slot names be lowerCamelCase, as CO's are.[^schema-collections.yaml] The schema declares five slots that link back to a collection (`elementOf`, `itemOf`, `itemContentOf`, `firstItemOf`, `lastItemOf`), and no class uses them.

## As the bundle's domain schema

`project.justfile` passes one root to `lokf adapt`, `Collection`, so a concept may be a `Collection`, a `Set`, a `Bag` or a `List`. Its comment says that the recipe names the root because the schema has no identifier slot, and that the items stay plain classes.[^project.justfile] The copy's notes say that `lokf adapt` re-rooted `Collection` on `lokf:Concept` and renamed nothing.[^lokf-collections.yaml] The `schema :=` line of `.lokf/justfile` and the `[tool.lokf]` table of `.lokf/pyproject.toml` both name the copy.

[Names and IRIs](../explanations/names-and-iris.md) says why three names differ from CO's, and [Scope and rules](../explanations/scope-and-rules.md) lists the rules the tests check instead of the validator.

[^schema-collections.yaml]: src/collections/schema/collections.yaml, the header, the slots and the classes
[^project.justfile]: project.justfile, the knowledge bundle recipes
[^lokf-collections.yaml]: .lokf/collections.yaml, the notes
