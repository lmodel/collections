<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# collections

Collections Ontology (CO) 2.0 (LinkML)

> **Two ways in.** This README is one; the other is a docent, a museum's name
> for a guide. Install
> [`ktl-docent`](https://github.com/noelmcloughlin/knowledge-trust-ladder) into
> whatever agent you already use, by a route from
> [the install page](https://w3id.org/ktl/docs/install/), and ask it anything
> about this project. It answers from `.lokf/knowledge/`,
> the checked part of what the project knows, and says how far each answer has
> been trusted (still a draft, checked by automation only, or confirmed by a
> named person). It opens the source for exact values, and records what it
> could not answer so the gap gets filled. The same docent serves a person at a
> prompt, an agent reading this file, or a chatbot that can load a skill.
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt`
> says how to weigh it.

## Documentation Website

[https://lmodel.github.io/collections](https://lmodel.github.io/collections)

## What it models

The schema renders the [Collections Ontology (CO)](https://github.com/collections-ontology/collections-ontology) 2.0 by Paolo Ciccarese and Silvio Peroni, as its OWL file `collections.owl` gives it at commit `619e7b0` of its repository. Every class and slot keeps CO's name and its IRI under `http://purl.org/co/`. The schema holds:

* **Collections** (`Collection`): a group of things taken as a whole, with its elements and its size. A collection is a **set** (`Set`), which holds each element once, or a **bag** (`Bag`), which may hold an element more than once through its items.
* **Lists** (`List`): a bag whose items are in order, with a first and a last item.
* **Items** (`CoItem`, `ListItem`): the entries of a bag, each wrapping one element. A list's item also has its place (`co_index`, from 1) and may link to the items before and after it.

Three names differ from CO's: `CoItem` for CO's `Item` and `co_size` for its `size`, as in lmodel/uco, and `co_index` for its `index`. [docs/about.md](docs/about.md) says why. The schema header's `version` is 2.0, CO's `owl:versionInfo`, and its `source` is CO's repository. `src/collections/schema/upstream/collections.owl` is CO's file, unchanged and matched by hash, and `tests/test_upstream.py` holds the schema to it. A weekly workflow reports when the repository moves, the file changes or a licence appears.

A link to an item, such as `firstItem` or `nextItem`, holds a copy of that item, since items have no IRI here. No validator checks a list's order or a collection's size; `tests/test_data.py` checks both over the examples, and [docs/index.md](docs/index.md) lists the rules.

## Influences

None beyond CO: the schema renders one ontology, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

None. CO's own `alignment.owl` aligns it with older collection vocabularies, which this repository does not render. CO states no mapping to RDF's containers, `rdf:Bag`, `rdf:Seq` and `rdf:List`, which hold their members another way, so the schema names none either.

## Not modelled here

* The links back from an element or an item to its collection (`elementOf`, `itemOf`, `itemContentOf`, `firstItemOf`, `lastItemOf`): they are declared, and no class uses them.
* CO's property chains, SWRL rules and narrower-property axioms. The tests check what they imply.
* CO's alignments and its example files.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/collections/schema/](src/collections/schema): the LinkML schema, `collections.yaml` (edit this), and CO's file in `upstream/`
* [src/collections_linkml/datamodel/](src/collections_linkml/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/collections.yaml`, which `lokf adapt` writes from `src/collections/schema/collections.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-collections.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. The copy roots `Collection` on `Concept`, so a concept may name it or any of its subclasses as its `type`. In Obsidian, add these classes to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
Collection, Set, Bag, List
```

A concept of one of these types writes its `element`, `co_size` and, for a bag or a list, its `item` entries inline. A name and a description are the concept's own `title` and `description`.

A host imports the copy beside LOKF's schema, `lokf.yaml`, and beside other adapt copies. LinkML merges them into one namespace, where the last definition of a name wins silently. So no class, enum or type shares a name with LOKF's or with the released copies of slsa, github-actions, oscal, spdx, nist-sp-800-218, nist-sp-800-53, nist-sp-800-171, nist-csf-v2, in-toto, cis-controls, iso27001, stix and attack.

One key is shared: `element`, which the spdx copy uses for an SPDX element's members under SPDX's IRI. A host that imports both copies has one `element` project under the other's IRI, until `lokf adapt` can rename a key that a neighbour defines ([lokf issue #169](https://github.com/nicholsn/lokf/issues/169), `--beside`). `tests/test_schema_rules.py` lists that key and fails on a new one. lmodel/uco's `uco_co` module renders the CO terms UCO uses, with the same names and IRIs; import that copy or this one, not both, until uco imports this schema in its place.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

The knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares.

CO's repository states no licence. The project's Google Code archive gives the Apache License 2.0 for its code, which held CO's OWL file, and CC BY 3.0 for its other content, such as its wiki, so this repository copies the OWL file under the Apache License. [NOTICE](NOTICE) gives the credit. This is not an official CO project, and its use implies no endorsement by CO's authors.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
