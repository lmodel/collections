---
type: Service
id: https://w3id.org/lmodel/collections/knowledge/services/documentation-site
genre: reference
title: Documentation website
description: The knowledge website at `https://lmodel.github.io/collections`, an Astro Starlight site in `website/` built from the README, `docs/`, the schema's pages and the bundle, which redirects the 2023 mkdocs site's element pages and `/about` to their successors.
resource: website/site.config.mjs
sources:
  - id: site.config.mjs
    resource: website/site.config.mjs
    title: the site address, DOCS and REDIRECTS
  - id: website-readme.md
    resource: website/README.md
    title: the build and the deploy
  - resource: website
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
---

# Documentation website

`website/` is the ktl-website site, served at `https://lmodel.github.io/collections`. It shows:

- the README as its home page;
- the pages in `docs/`;
- a page per schema element from `docs/elements/`;
- a page per concept of the bundle, with its trust label.[^site.config.mjs]

`npm run build` runs the sync, builds the site and checks every link. `website/README.md` says how it builds and deploys.[^website-readme.md]

`REDIRECTS` keeps the addresses of the retired mkdocs site of 2023, which served each element at the site root, and the `/elements/<name>/` addresses the w3id rules send a term to. Each leads to its successor's schema page: `_index` to `co_index`, `size` to `co_size`, and `Thing`, `PositiveInteger` and `types` to the schema's index.

[^site.config.mjs]: website/site.config.mjs, the site address, DOCS and REDIRECTS
[^website-readme.md]: website/README.md, the build and the deploy
