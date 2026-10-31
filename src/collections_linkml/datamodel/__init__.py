"""Data model package for collections."""

from pathlib import Path
from .collections import *  # noqa: F403

THIS_PATH = Path(__file__).parent

# A wheel carries the schema in the package's schema folder; a source checkout
# keeps it at src/collections/schema, the path w3id.org serves.
SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
if not SCHEMA_DIRECTORY.is_dir():
    SCHEMA_DIRECTORY = THIS_PATH.parents[1] / "collections" / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "collections.yaml"
