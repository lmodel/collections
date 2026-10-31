# config.public.mk

# This file is public in git. No sensitive info allowed.

###### schema definition variables, used by justfile

# Note:
# - just works fine with quoted variables of dot-env files like this one
LINKML_SCHEMA_NAME="collections"
LINKML_SCHEMA_AUTHOR="Noel McLoughlin <noel.mcloughlin@gmail.com>"
LINKML_SCHEMA_DESCRIPTION="Collections Ontology (CO): LinkML Schema"
LINKML_SCHEMA_SOURCE_DIR="src/collections/schema"

# The schema keeps the name collections and the path that w3id.org/lmodel/collections
# serves, src/collections/schema/collections.yaml. A Python package of that name
# would shadow the standard library's collections module, so the data model's
# package is collections_linkml.
LINKML_PYTHON_PACKAGE="collections_linkml"

###### linkml generator variables, used by justfile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=config.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS=

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile=rdfs)
# LINKML_GENERATORS_OWL_ARGS="--no-type-objects --no-metaclasses --metadata-profile=rdfs"
LINKML_GENERATORS_OWL_ARGS=

## pass args to pydantic generator which isn't supported by gen-project
## https://github.com/linkml/linkml/issues/2537
LINKML_GENERATORS_PYDANTIC_ARGS=
