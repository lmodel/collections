# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Added

- **A LinkML schema of the Collections Ontology (CO) 2.0, with CO's own names and IRIs.** It holds collections, sets, bags and lists, and the items of a bag or a list, with the constraints LinkML can state. Tests check CO's other rules, such as a list's order, over the examples.
- **CO 2.0's OWL file, copied unchanged and matched by hash, and a weekly upstream watch**, which reports a new commit, a changed or dropped file, another edition, a licence that appears, or a check that could not finish.
- **`.lokf/collections.yaml`, the schema's `lokf adapt` copy, rooted on `Collection`.** The knowledge release attaches it as `schema-<tag>-collections.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of thirteen released lmodel copies.
- **An example of each class and a counter-example for each constraint**, held to the validator by `just test`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **The project moves from linkml-project-cookiecutter to linkml-project-copier v0.5.0.** The Python project is `collections-linkml` and its package `collections_linkml`, since a package named `collections` would shadow Python's own. The schema keeps its name, `collections`, and its path. PyPI publishing stays off.
- **CO's `Item`, `size` and `index` are `CoItem`, `co_size` and `co_index`**, with CO's IRIs, so they clash neither with UCO's terms nor with the schema's index page.

### Removed

- **The `Thing` class and the `positive integer` type, and the mappings to Allotrope, NCIT, SIO, SUMO, Wikidata and schema.org.** CO states none of the mappings.
- **The PyPI publishing workflow and the mkdocs site.** The knowledge website replaces the site.
