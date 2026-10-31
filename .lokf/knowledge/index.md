---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/collections/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: collections Knowledge Bundle
description: Collections Ontology (CO) 2.0 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/collections/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# collections Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for collections. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation website](services/documentation-site.md) - The knowledge website at `https://lmodel.github.io/collections`, an Astro Starlight site in `website/` built from the README, `docs/`, the schema's pages and the bundle, which redirects the 2023 mkdocs site's element pages and `/about` to their successors.

# Datasets

* [collections LinkML schema](datasets/collections-linkml-schema.md) - The LinkML schema of the Collections Ontology (CO) 2.0, `src/collections/schema/collections.yaml` (schema id `https://w3id.org/lmodel/collections`, version 2.0): six classes and sixteen slots, each with CO's name and IRI. Its `lokf adapt` copy `.lokf/collections.yaml`, rooted on `Collection`, is the bundle's domain schema.
* [Copy of CO's OWL file](datasets/collections-ontology-copy.md) - `src/collections/schema/upstream/collections.owl`, the Collections Ontology 2.0's OWL file copied unchanged from commit `619e7b0` of its GitHub repository and matched by its git object hash, which the tests hold the schema to.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the schema: the twelve formats in `project/`, the Python dataclasses and Pydantic models in `src/collections_linkml/datamodel/`, the merged schema in `docs/schema/` and the element pages in `docs/elements/`.
* [Tests and example data](datasets/test-data.md) - The tests under `tests/`: 12 valid examples, 11 counter-examples the validator rejects and 14 that break a rule only a test checks, the checks against CO's OWL file and the watch's stubbed answers, and the 13 released neighbour copies the adapt copy is held apart from.

# References

* [The Collections Ontology (CO) 2.0](references/collections-ontology.md) - The Collections Ontology 2.0 by Paolo Ciccarese and Silvio Peroni (ontology IRI `http://purl.org/co`): sets, bags and lists in OWL 2 DL, published in GitHub's `collections-ontology/collections-ontology`, described in Semantic Web 5(6), 2014, and licensed Apache-2.0 for code and CC BY 3.0 for content by its Google Code archive.

# Glossary

* [Collection](glossary/collection.md) - A collection in the Collections Ontology (`coll:Collection`): a group of things taken as a whole, with its elements and its size; a set holds each element once, and a bag may hold one more than once.
* [Bag](glossary/bag.md) - A bag in the Collections Ontology (`coll:Bag`): a collection that may hold one element more than once, in no order, through items that each wrap one element.
* [List](glossary/list.md) - A list in the Collections Ontology (`coll:List`): a bag whose items are in order, each with its place from 1, a first and a last item, and links to the items before and after it.
* [Item](glossary/item.md) - An item in the Collections Ontology (`coll:Item`, the schema's `CoItem`): an entry of a bag that wraps one of the bag's elements in `itemContent`.

# Explanations

* [Names and IRIs](explanations/names-and-iris.md) - Why the schema keeps CO's names and IRIs under the `coll` prefix, why `CoItem`, `co_size` and `co_index` differ from CO's names, how the terms match lmodel/uco's `uco_co` module, and the one key, `element`, the adapt copy shares with spdx's.
* [Scope and rules](explanations/scope-and-rules.md) - What the schema renders of CO and leaves out, why a link to an item holds a copy of it, why it names no mapping, and the rules of CO that no validator checks, which the tests check over the examples instead.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: install with `uv sync --group dev`, edit `src/collections/schema/collections.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit the regenerated files.
* [Validate data](playbooks/validate-data.md) - How to check a collection, set, bag or list file against the schema with `linkml-validate`, and which of CO's rules only `tests/test_data.py` checks.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the upstream watch reports a new commit on CO's master branch, a changed or dropped `collections.owl`, another edition in `owl:versionInfo`, or a licence: replace the copy, move the pins in `scripts/check_upstream_release.py` and the schema header together, and run the tests.
* [Release](playbooks/release.md) - How a release is made: write `## [Unreleased]` in CHANGELOG.md, merge a `feat:`, `fix:` or `security:` change, and semantic-release tags it from the `v0.0.0` baseline, the first release being 0.1.0, after which Knowledge Release attaches the schema copy and the bundle.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Policies

* [Licence and attribution](policies/license-and-attribution.md) - The licences: Apache-2.0 for the schema and code, CC BY 4.0 for the knowledge bundle, Apache-2.0 for the copied CO file, which CO's Google Code archive gives for the project's code, and MIT for the copier template's scaffolding.
* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work in this repository: the contributor owns what they submit, every element renders a class or property of CO 2.0 cited by its axiom, CO's IRIs are kept, the copied OWL file stays CO's, and the scheduled librarian's changes go through a reviewed pull request.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, Mondays at 06:00 UTC and by hand, it runs ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its co-copy job runs `scripts/check_upstream_release.py` against CO's GitHub repository, and on a finding opens or updates the issue titled Upstream watch: the Collections Ontology has changed.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request its plan job says what a merge would release, and on a push to main its release job, in the release Environment, tags the release and dispatches Knowledge Release.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: it builds the site on pull requests and pushes that touch its inputs, Mondays at 05:23 UTC and by hand, and deploys it to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the bundle's gate, which validates `.lokf/` on pull requests, Mondays at 06:00 UTC and by hand, and checks that each new confirmation is backed by its person's approval or signed commit.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: Mondays at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`, it runs the ktl-librarian skill pinned to KTL v0.59.0 in a job with no write token and opens a pull request with what changed.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: on a published release once `KNOWLEDGE_RELEASE_ENABLED` is `true`, or by hand for a tag, it attaches the schema copy, the bundle zip and the Copilot skill zip, each with its checksum and attestation.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: Mondays at 04:10 UTC and by hand, it compares the sidecar's copies and the skills pin with the newest KTL release and opens one pull request when they are behind.
