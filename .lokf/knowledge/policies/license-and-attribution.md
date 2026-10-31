---
type: Policy
id: https://w3id.org/lmodel/collections/knowledge/policies/license-and-attribution
genre: reference
title: Licence and attribution
description: "The licences: Apache-2.0 for the schema and code, CC BY 4.0 for the knowledge bundle, Apache-2.0 for the copied CO file, which CO's Google Code archive gives for the project's code, and MIT for the copier template's scaffolding."
resource: NOTICE
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: readme.md
    resource: README.md
    title: the License section
  - resource: LICENSE
  - resource: website/NOTICE
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:10:16Z"
status: draft
---

# Licence and attribution

The schema and the code are under the Apache License 2.0, and the knowledge bundle under CC BY 4.0, as its `index.md` declares.[^readme.md]

NOTICE credits CO 2.0 to Paolo Ciccarese and Silvio Peroni and cites their paper by its DOI. It says that the schema's descriptions are this project's own words, and that `src/collections/schema/upstream/collections.owl` is CO's file, unchanged, copied under the Apache License, which the Google Code archive gives for the project's code. The archive gives CC BY 3.0 for the project's other content, such as its wiki. It also credits the linkml-project-copier template, under MIT, and the KTL templates, under Apache-2.0.[^notice]

[^readme.md]: README.md, the License section
[^notice]: NOTICE, every section
