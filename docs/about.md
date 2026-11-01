# About collections

This page is for anyone reading the [LinkML](https://linkml.io) schema's
elements: it says how they are named and what the model leaves out.

The Collections Ontology (CO) describes three kinds of collection. A set
holds each element once. A bag may hold an element more than once, through
items that each wrap one element. A list is a bag whose items have a place:
an index from 1, a first and a last item, and a next and a previous item.

Every class and slot of CO keeps CO's local name and CO's IRI, such as
`coll:Bag` for `http://purl.org/co/Bag`. Three names differ. CO's `Item` is
the class `CoItem` and CO's `size` is the slot `co_size`, as in the `uco_co`
module of lmodel/uco, because UCO defines terms of the same name. CO's
`index` is the slot `co_index`, because LinkML's documentation generator
writes the page of a slot named `index` over the schema's index page.
The prefix is `coll`, the one the LinkML prefix map gives CO's namespace.
That map gives `co` to another vocabulary. The descriptions are this
project's own words.

One class is not CO's: `CoElement`, a thing a collection holds, named by its
IRI, with an IRI of the schema's own. CO lets `element` and `itemContent`
hold anything. Ranging over `CoElement` makes their values links to
resources in RDF, and in the generated ontology, rather than text.

The mappings to other vocabularies are those CO's own `alignment.owl` states,
with ORE's namespace corrected to the one ORE defines its terms under, and a
few close mappings to schema.org's lists, which are this project's own.

## What is left out

- The links from an element or an item back to its collection
  (`elementOf`, `itemOf`, `itemContentOf`, `firstItemOf`, `lastItemOf`) are
  declared, but no class uses them, since each collection holds its items.
- CO's SWRL rules, which derive one link from others, and the
  narrower-property axioms on single-valued slots, such as `firstItem` under
  `item`. LinkML's inheritance is monotonic, so a slot under a multivalued
  parent is multivalued too.
  CO's two property chains are stated as `path_rule`s, which no generator
  reads. The tests check what the chains and rules imply, as the index page
  lists.
- CO's example files.

## Reference

- [The Collections Ontology on GitHub](https://github.com/collections-ontology/collections-ontology)
- Paolo Ciccarese and Silvio Peroni, "The Collections Ontology: creating and
  handling collections in OWL 2 DL frameworks", Semantic Web 5(6), 2014,
  [doi:10.3233/SW-130121](https://doi.org/10.3233/SW-130121)
