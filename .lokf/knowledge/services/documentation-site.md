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
  at: "2026-11-15T02:33:52Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-01T00:01:52Z"
---

# Documentation website

`website/` is the ktl-website site, served at `https://lmodel.github.io/collections`. It shows:

- the README as its home page;
- the pages in `docs/`;
- a page per schema element from `docs/elements/`;
- a page per concept of the bundle, with its trust label.[^site.toml]

`npm run build` runs the sync, builds the site and checks every link. `website/README.md` says how it builds and deploys.[^website-readme.md]

`REDIRECTS` keeps the addresses of the retired mkdocs site of 2023, which served each element at the site root, and the `/elements/<name>/` addresses the w3id rules send a term to. Each leads to its successor's schema page: `_index` to `co_index`, `size` to `co_size`, and `Thing`, `PositiveInteger` and `types` to the schema's index.

[^site.toml]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md, the build and the deploy
