---
type: Dataset
id: https://w3id.org/lmodel/collections/knowledge/datasets/collections-alignment-copy
genre: reference
title: Copy of CO's alignment file
description: "`src/collections/schema/upstream/alignment.owl`, CO's alignment with SWAN Collections 1.2, the ontologydesignpatterns.org patterns, the Music Ontology and OAI-ORE, copied unchanged from commit `619e7b0` and matched by its git object hash; the schema's exact, narrow and broad mappings follow it."
resource: src/collections/schema/upstream/alignment.owl
derivedFrom:
  - https://w3id.org/lmodel/collections/knowledge/references/collections-ontology
sources:
  - id: alignment.owl
    resource: src/collections/schema/upstream/alignment.owl
    title: the owl:Ontology header and the alignment axioms
  - id: notice
    resource: NOTICE
    title: the paragraph on alignment.owl
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the alignment tests
  - id: readme.md
    resource: README.md
    title: the Mappings section
generated:
  by: process:ktl-librarian
  at: "2026-11-01T00:01:52Z"
status: draft
---

# Copy of CO's alignment file

`src/collections/schema/upstream/alignment.owl` is CO's alignment file in RDF/XML, titled "Alignments between CO and other models" and dated May 30, 2011. It imports CO, SWAN Collections 1.2 and five ontologydesignpatterns.org patterns: Bag, Collection Entity, List, Sequence and Set. It states which of their classes and properties are the same as CO's, and which classes and properties of the Music Ontology and OAI-ORE are narrower than CO's.[^alignment.owl]

NOTICE says that the file is copied unchanged from the same commit as CO's OWL file, git object `f6d6457b9b323e3e4bdf54ffeec5bc59f878f7ac`, and that it is the same file as in the archived Subversion trunk.[^notice]

`tests/test_upstream.py` checks the copy's hash, and checks that each class and slot's exact, narrow and broad mappings, other than those to schema.org, are the ones the file states for CO's IRI.[^test_upstream.py] The file writes ORE's namespace as `http://www.openarchives.org/ore/items/`, and the mappings use `http://www.openarchives.org/ore/terms/`, where ORE defines those terms.[^readme.md]

[^alignment.owl]: src/collections/schema/upstream/alignment.owl, the owl:Ontology header and the alignment axioms
[^notice]: NOTICE, the paragraph on alignment.owl
[^test_upstream.py]: tests/test_upstream.py, the alignment tests
[^readme.md]: README.md, the Mappings section
