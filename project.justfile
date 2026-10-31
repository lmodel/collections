## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/collections.yaml` is the copy `lokf adapt` writes from the schema
# so that it can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the
# moves). The roots are the classes a knowledge concept may name as its
# type: Collection, so that a concept may be a Collection, a Set, a Bag or a
# List, and CoElement, the thing a collection holds, whose iri becomes LOKF's
# id. Adapt would take only CoElement as a root, the one class with an
# identifier, so the recipe names both. CoItem and ListItem are the values a
# bag or a list holds inline, so they stay plain classes. The recipes run the `lokf` the sidecar's floor
# pins (0.9.0 or later); LOKF_CMD runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root Collection --root CoElement"

# Rewrite .lokf/collections.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/collections.yaml

# Fail when .lokf/collections.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/collections.yaml --check
