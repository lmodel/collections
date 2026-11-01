<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# collections

Collections Ontology (CO) 2.0 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/collections](https://lmodel.github.io/collections)

## What it models

The schema renders the [Collections Ontology (CO)](https://github.com/collections-ontology/collections-ontology) 2.0 by Paolo Ciccarese and Silvio Peroni, from its OWL file `collections.owl` at commit `619e7b0`. It holds collections, sets, bags and lists, their items, and the elements they hold (`CoElement`, the one class CO lacks, so that in RDF a collection links to its elements). Every class and slot keeps CO's IRI under `http://purl.org/co/`, and [docs/about.md](docs/about.md) says why three names differ from CO's.

`src/collections/schema/upstream/collections.owl` is CO's file, unchanged, and `tests/test_upstream.py` holds the schema to it. A weekly workflow reports when the repository moves, the file changes or a licence appears. No validator checks a list's order or a collection's size, so `tests/test_data.py` checks both over the examples.

## Mappings

* **CO's alignment**: the exact, narrow and broad mappings to SWAN Collections 1.2, the ontologydesignpatterns.org patterns, the Music Ontology and OAI-ORE come from CO's own `alignment.owl`, copied unchanged to `src/collections/schema/upstream/`. The ORE mappings use `http://www.openarchives.org/ore/terms/`, where ORE defines those terms.
* **schema.org**: the close and broad mappings to `ItemList` and `ListItem` are this project's own.

## Not modelled here

* The links back from an element or an item to its collection (`elementOf`, `itemOf`, `itemContentOf`, `firstItemOf`, `lastItemOf`): the schema declares them, but no class uses them.
* CO's SWRL rules, and the narrower-property axioms on single-valued slots, such as `firstItem` under `item` and `nextItem` under `followedBy`: LinkML's inheritance is monotonic, so a slot under a multivalued parent is multivalued too. `followedBy` and `precededBy` name `nextItem` and `previousItem` as their `transitive_form_of`, and `firstItemOf` and `lastItemOf` are narrower forms of `itemOf`. CO's two property chains are `path_rule`s on `element` and `item`, which no generator reads. The tests check what the chains and rules imply.
* CO's example files.

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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/collections.yaml`, is the copy `just lokf-adapt` writes from `src/collections/schema/collections.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-collections.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots `Collection` and `CoElement` on `Concept`, so a concept may name either, or a subclass of `Collection`, as its `type`. In Obsidian, add these classes to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
Collection, Set, Bag, List, CoElement
```

A concept of one of these types writes its `element`, `co_size` and, for a bag or a list, its `item` entries inline.

No class, enum or type of the copy shares a name with LOKF's schema or with the lmodel copies in `tests/neighbours/`. One key is shared: spdx's copy also defines `element`, under SPDX's IRI, so a host that imports both has one `element` project under the other's IRI. `tests/test_schema_rules.py` lists that key and fails on a new one, and [lokf #169](https://github.com/nicholsn/lokf/issues/169) asks `adapt` for a `--beside` option that would rename it. lmodel/uco's `uco_co` module renders the CO terms UCO uses: import that copy or this one, not both.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

CO's repository states no licence, and its Google Code archive gave the Apache License 2.0 for the code that held the OWL file, so this repository copies that file under the Apache License. [NOTICE](NOTICE) gives the credit. This is not an official CO project, and its use implies no endorsement by CO's authors.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
