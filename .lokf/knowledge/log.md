# Change Log

## 2026-10-31

* **Changed**: the README now says `uco_co` keeps the same names but `index`, which is `co_index` here, and the schema gives its naming reasons in the header notes.
* **Prose**: reworded 7 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: NOTICE now says the copied OWL file falls under CO's code licence, Apache-2.0, and that CC BY 3.0 covers CO's other content.
* **Changed**: SECURITY.md now says the watch's token can also write issues, and that the watch follows a redirect only to GitHub.
* **Changed**: `tests/data/valid/` now holds 12 examples, two of them lists whose items are written only as a first, a last or a next item.
* **Prose**: reworded 11 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Added**: collections LinkML schema, from `src/collections/schema/collections.yaml` and its adapt copy.
* **Added**: Copy of CO's OWL file, from `src/collections/schema/upstream/collections.owl` and NOTICE.
* **Added**: Generated artefacts, from the justfile, `.linkml/generators.yaml` and `config.public.mk`.
* **Added**: Tests and example data, from `tests/`.
* **Added**: The Collections Ontology (CO) 2.0, from its repository, its paper's record and its Google Code archive.
* **Added**: Collection, from the schema.
* **Added**: Bag, from the schema.
* **Added**: List, from the schema.
* **Added**: Item, from the schema.
* **Added**: Names and IRIs, from `docs/about.md`, the README and the schema's comments.
* **Added**: Scope and rules, from `docs/index.md`, `docs/about.md` and the README.
* **Added**: Regenerate and test, from CONTRIBUTING.md and the justfile.
* **Added**: Validate data, from `docs/index.md`.
* **Added**: Update the upstream pins, from the watch script.
* **Added**: Release, from CONTRIBUTING.md, `.releaserc.json` and CHANGELOG.md.
* **Added**: Licence and attribution, from NOTICE and the README.
* **Added**: Security policy, from SECURITY.md and the Dependabot settings.
* **Added**: AI covenant, from AI_COVENANT.md.
* **Added**: Documentation website, from `website/site.config.mjs` and `website/README.md`.
* **Added**: Build and test (main.yaml).
* **Added**: Lint & docs (lint-and-docs.yaml).
* **Added**: Upstream watch (upstream-watch.yaml).
* **Added**: Semantic release (semantic-release.yml).
* **Added**: Knowledge website (knowledge-website.yaml).
* **Added**: Knowledge Registrar (knowledge-registrar.yaml).
* **Added**: Knowledge Librarian (knowledge-librarian.yaml).
* **Added**: Knowledge Release (knowledge-release.yaml).
* **Added**: Knowledge sync (knowledge-sync.yaml).
* **Added**: Knowledge sources map, with each source, what it yields and how to re-check it.
* **Removal**: the sidecar's example service A, which the real concepts replace.
* **Removal**: the sidecar's example service B, which the real concepts replace.
* **Initialization**: Scaffolded the LOKF bundle for collections with placeholder
  services. Real concepts to follow.
