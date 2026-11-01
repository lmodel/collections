---
type: Dataset
id: https://w3id.org/lmodel/collections/knowledge/datasets/collections-ontology-copy
genre: reference
title: Copy of CO's OWL file
description: "`src/collections/schema/upstream/collections.owl`, the Collections Ontology 2.0's OWL file copied unchanged from commit `619e7b0` of its GitHub repository and matched by its git object hash, which the tests hold the schema to."
resource: src/collections/schema/upstream/collections.owl
version: "2.0"
derivedFrom:
  - https://w3id.org/lmodel/collections/knowledge/references/collections-ontology
sources:
  - id: collections.owl
    resource: src/collections/schema/upstream/collections.owl
    title: the owl:Ontology header
  - id: notice
    resource: NOTICE
    title: the Collections Ontology section
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the module docstring and the tests
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:56:19Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-11-01T00:01:52Z"
---

# Copy of CO's OWL file

`src/collections/schema/upstream/collections.owl` is CO 2.0's OWL file in RDF/XML. Its header gives the ontology IRI `http://purl.org/co`, `owl:versionInfo` 2.0 and the date March 19, 2012, and imports the error ontology at `http://purl.org/spar/error`.[^collections.owl]

NOTICE says that the file is copied unchanged from commit `619e7b02646321174635fd04be658e338bf7d1d7` of `collections-ontology/collections-ontology`, git object `4e19e4892212de2b1805923a7a69fa4ba8c1b424`. It also says that the file differs from the archived Subversion trunk in one line, the address of the error ontology.[^notice]

`tests/test_upstream.py` checks the copy's hash. It also checks that the schema renders every class and property the file declares, with CO's domains, ranges, cardinalities, inverses, transitive properties, superclasses and disjoint classes.[^test_upstream.py] The upstream watch compares the file on CO's master branch with the same pin.

[^collections.owl]: src/collections/schema/upstream/collections.owl, the owl:Ontology header
[^notice]: NOTICE, the Collections Ontology section
[^test_upstream.py]: tests/test_upstream.py, the module docstring and the tests
