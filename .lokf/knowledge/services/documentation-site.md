---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/services/documentation-site
genre: reference
title: Documentation website
description: The knowledge website at `https://lmodel.github.io/collections`, a Hugo site in `website/` built from the README, `docs/`, the schema's pages and the bundle, which redirects the 2023 mkdocs site's element pages and `/about` to their successors.
resource: website/site.toml
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme.md
    resource: website/README.md
    title: the build and the deploy
  - resource: website
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:01:58Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-01T00:01:52Z"
---

# Documentation website

`website/` is the ktl-website site, a Hugo site served at `https://lmodel.github.io/collections`.[^site.toml] It shows:

- the README as its home page;
- the pages in `docs/`;
- a page per class, slot, enumeration and type of `src/collections/schema/collections.yaml`, written by LinkML's `gen-doc`, each also at `elements/<Name>/`;
- a page per concept of the bundle, with its trust label.[^website-readme.md]

`scripts/build.sh`, run in `website/`, writes the site to `dist/` with its search index and then checks every link between its pages. Hugo and Pagefind come from PyPI through uv, so the build needs bash, git and uv. `scripts/build.sh serve` serves the site at `http://localhost:1313/collections/` and rebuilds it as you edit.[^website-readme.md]

The redirects in `website/site.toml` keep the addresses of the retired mkdocs site of 2023, which served each element at the site root, and four `/elements/<name>/` addresses the w3id rules send a term to. Each leads to its successor's page: `size` to `co_size`, `Thing`, `PositiveInteger`, `types` and `collections` to the schema's index, and `about` to `docs/about.md`.[^site.toml]

[^site.toml]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md, the build and the deploy
