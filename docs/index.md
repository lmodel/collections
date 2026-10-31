# collections

This project is a LinkML model of the Collections Ontology (CO) 2.0 by Paolo
Ciccarese and Silvio Peroni. It keeps CO's class and property names and
their IRIs under `http://purl.org/co/`. A collection is a set, a bag or a
list, and a bag or a list holds its elements through items.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [`collections.yaml`](schema/collections.yaml): the schema

## Validating data

`linkml-validate -s src/collections/schema/collections.yaml -C List list.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it.

No validator checks these rules of CO, so `tests/test_data.py` checks them
over every example:

- A set holds no element twice.
- A collection's size, where it is given, is the number of its elements for
  a set, and of its items for a bag or a list.
- Where a bag gives its elements, each item's content is one of them.
- A list's items are its `item` entries, its `firstItem` and `lastItem`, and
  the `nextItem` of each. CO makes the first and the last item narrower forms
  of `item`, and the next item of an item is an item of the same list.
- A list's indexes count 1, 2, 3 and on, with no gap or repeat.
- `firstItem` is a copy of the item with index 1, which has no previous item.
  `lastItem` is a copy of the item with the highest index, which has no next
  item.
- An item's `nextItem` and `previousItem` are copies of the items one place
  after and before it. Its `followedBy` and `precededBy` hold only items after
  and before it.

The counter-examples in `tests/data/problem/invalid/` break one rule each.

Items have no IRI in this model, so a link to an item holds a copy of it. In
RDF each copy is then a node of its own, where CO's own examples name each
item by its IRI and link to that one node.
