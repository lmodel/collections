# Explanations

* [Names and IRIs](names-and-iris.md) - Why the schema keeps CO's names and IRIs under the `coll` prefix, why `CoItem`, `co_size` and `co_index` differ from CO's names, why `CoElement` has an IRI of its own, how the terms match lmodel/uco's `uco_co` module, and the one key, `element`, the adapt copy shares with spdx's.
* [Scope and rules](scope-and-rules.md) - What the schema renders of CO, adds to it (`CoElement`) and leaves out, why a link to an item holds a copy of it, where its mappings come from, and the rules of CO that no validator checks, which the tests check over the examples instead.
