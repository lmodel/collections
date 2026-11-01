---
type: Dataset
id: https://w3id.org/lmodel/collections/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the schema: the twelve formats in `project/`, the Python dataclasses and Pydantic models in `src/collections_linkml/datamodel/`, the merged schema in `docs/schema/` and the element pages in `docs/elements/`."
resource: project
sources:
  - id: justfile
    resource: justfile
    title: the gen-project and gen-doc recipes
  - id: config.public.mk
    resource: config.public.mk
    title: the schema, package and gen-owl variables
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the jsonschema and owl settings
generated:
  by: process:ktl-librarian
  at: "2026-11-01T00:01:52Z"
status: draft
---

# Generated artefacts

`just gen-project` runs LinkML's generators on the schema with the settings in `.linkml/generators.yaml`, and writes `project/`. It moves the Python dataclasses to `src/collections_linkml/datamodel/collections.py` and writes the Pydantic models beside them, then runs gen-java, gen-typescript and gen-owl on their own.[^justfile] `just gen-doc` writes the merged schema to `docs/schema/collections.yaml` and the element pages to `docs/elements/`, which git ignores.

`config.public.mk` names the schema `collections` at `src/collections/schema/` and the package `collections_linkml`, since a package named `collections` would shadow Python's own.[^config.public.mk] The JSON Schema generator lists each range's subclasses, so a bag may hold list items.[^generators.yaml] `config.public.mk` passes `--no-use-native-uris` to gen-owl, and `.linkml/generators.yaml` sets `use_native_uris: false`, so the ontology describes CO's IRIs, such as `coll:Bag`, rather than IRIs of the schema's own.[^config.public.mk]

`project/` holds Excel, GraphQL, Java, JSON-LD, JSON Schema, OWL, a prefix map, Protobuf, SHACL, ShEx, SQL and TypeScript files. They are generated: regenerate them, never edit them.

[^justfile]: justfile, the gen-project and gen-doc recipes
[^config.public.mk]: config.public.mk, the schema and package variables
[^generators.yaml]: .linkml/generators.yaml, the jsonschema settings
