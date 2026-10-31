"""Data test."""

import glob
import json
import os
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader

import collections_linkml.datamodel.collections

ROOT = Path(__file__).parent.parent
DATA = Path(__file__).parent / "data"
DATA_DIR_VALID = DATA / "valid"
DATA_DIR_INVALID = DATA / "invalid"
# Counter-examples of rules the validator cannot check; `rule_faults` checks them.
DATA_DIR_RULES = DATA / "problem" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml"))
RULE_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_RULES, "*.yaml"))

SCHEMA = ROOT / "src" / "collections" / "schema" / "collections.yaml"
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "collections.schema.json"


def _class(filepath):
    return Path(filepath).stem.split("-")[0]


def _fails_at(filepath):
    """The place a counter-example names on its first line, as `# Fails at: /key`."""
    first = Path(filepath).read_text().splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{filepath}: the first line names where it fails, as # Fails at: /key"
    )
    return first.removeprefix("# Fails at: ").strip()


def test_the_example_folders_hold_examples():
    """The parametrized tests below pass on an empty folder, so this one does not."""
    counts = [len(VALID_EXAMPLE_FILES), len(INVALID_EXAMPLE_FILES)]
    counts.append(len(RULE_EXAMPLE_FILES))
    assert all(n >= least for n, least in zip(counts, (13, 12, 14))), counts


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    tgt_class = getattr(collections_linkml.datamodel.collections, _class(filepath))
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


# The JSON Schema the validator generates is the one check that applies every
# constraint the schema states, so each example is held to it: a valid one
# must pass, and a counter-example must fail.
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files_validate(filepath):
    """Every valid example passes the validator."""
    data = yaml.safe_load(Path(filepath).read_text())
    report = validate(data, str(SCHEMA), _class(filepath))
    assert not report.results, [r.message for r in report.results]


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files_fail(filepath):
    """Every counter-example fails the validator at the place its first line
    names, and only there, so a file that starts failing for another reason
    fails this test."""
    pointer = _fails_at(filepath)
    data = yaml.safe_load(Path(filepath).read_text())
    messages = [
        r.message for r in validate(data, str(SCHEMA), _class(filepath)).results
    ]
    assert messages, f"{filepath} passes the validator"
    assert all(m.endswith(f" in {pointer}") for m in messages), messages


def _committed_validator(class_name):
    """A validator for one class of the committed project/jsonschema file,
    under the draft the file names."""
    schema = json.loads(JSON_SCHEMA.read_text())
    root = {"$schema": schema["$schema"], "$ref": f"#/$defs/{class_name}"}
    root["$defs"] = schema["$defs"]
    return jsonschema.validators.validator_for(schema)(root)


def _pointer(error):
    return "/" + "/".join(str(p) for p in error.absolute_path)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES + INVALID_EXAMPLE_FILES)
def test_committed_json_schema_agrees(filepath):
    """The committed JSON Schema, the file a consumer takes, accepts every
    valid example and rejects each counter-example at the place it names."""
    data = yaml.safe_load(Path(filepath).read_text())
    errors = list(_committed_validator(_class(filepath)).iter_errors(data))
    if filepath in VALID_EXAMPLE_FILES:
        assert not errors, [e.message for e in errors]
    else:
        assert errors and {_pointer(e) for e in errors} == {_fails_at(filepath)}


def test_every_class_has_an_example():
    """Each class has a valid example: the four a knowledge-bundle concept may
    name as its type, the two item classes they hold, and the CoElement an item
    wraps."""
    classes = set(yaml.safe_load(SCHEMA.read_text())["classes"])
    examples = {_class(f) for f in VALID_EXAMPLE_FILES}
    assert classes <= examples, sorted(classes - examples)


# The rules of CO that no validator checks, which docs/index.md lists. Each
# fault is the JSON pointer of the place that breaks a rule, in the form the
# validator reports, so a counter-example names it the same way.
COLLECTIONS = ("Collection", "Set", "Bag", "List")


def _same(copy, item):
    """Whether a copy names the same item: the same place and the same content."""
    return (
        item is not None
        and copy.get("co_index") == item.get("co_index")
        and copy.get("itemContent") == item.get("itemContent")
    )


def _link_faults(item, at, by_index):
    """The faults of an item's links, and of the links of every copy it holds.
    `by_index` maps each index of the item's list to the item there, or is
    None for an item on its own, whose links are checked by index alone."""
    faults = []
    own = item.get("co_index")
    links = [("nextItem", item.get("nextItem"), lambda i: i == own + 1)]
    links.append(("previousItem", item.get("previousItem"), lambda i: i == own - 1))
    for name, rule in (
        ("followedBy", lambda i: i > own),
        ("precededBy", lambda i: i < own),
    ):
        links += [
            (f"{name}/{n}", copy, rule) for n, copy in enumerate(item.get(name) or [])
        ]
    for name, copy, rule in links:
        if copy is None:
            continue
        if not rule(copy["co_index"]) or (
            by_index is not None and not _same(copy, by_index.get(copy["co_index"]))
        ):
            faults.append(f"{at}/{name}")
        faults += _link_faults(copy, f"{at}/{name}", by_index)
    return faults


def _list_items(data):
    """A list's items by their index, each with the first place it is written,
    as CO's axioms give them: the entries of `item`; `firstItem` and
    `lastItem`, which CO makes narrower forms of `item`; and the `nextItem` of
    each of them, by CO's chain item o nextItem. An index takes the first item
    written at it, the entries of `item` first, so a link that disagrees is
    left to the link checks. The faults are the entries of `item` that repeat
    an index."""
    faults, by_index = [], {}
    items = data.get("item") or []
    for n, item in enumerate(items):
        if item["co_index"] in by_index:
            faults.append(f"/item/{n}/co_index")
        by_index.setdefault(item["co_index"], (item, f"/item/{n}"))
    linked = [(data.get(name), f"/{name}") for name in ("firstItem", "lastItem")]
    linked += [(item, f"/item/{n}") for n, item in enumerate(items)]
    while linked:
        item, at = linked.pop(0)
        if item is not None:
            by_index.setdefault(item["co_index"], (item, at))
            linked.append((item.get("nextItem"), f"{at}/nextItem"))
    return by_index, faults


def _list_faults(data, by_index):
    """A list's order: indexes 1 to n, each once, and every link agreeing."""
    items = {index: item for index, (item, _) in by_index.items()}
    faults = [
        f"/item/{n}/co_index"
        for n, item in enumerate(data.get("item") or [])
        if item["co_index"] > len(items)
    ]
    for name, index in (("firstItem", 1), ("lastItem", len(items))):
        if data.get(name) is not None:
            if not _same(data[name], items.get(index)):
                faults.append(f"/{name}")
            faults += _link_faults(data[name], f"/{name}", items)
    for n, item in enumerate(data.get("item") or []):
        faults += _link_faults(item, f"/item/{n}", items)
    return faults


def rule_faults(class_name, data):
    """Every place at which an example of the class breaks a rule of CO that
    no validator checks."""
    if class_name == "ListItem":
        return _link_faults(data, "", None)
    if class_name not in COLLECTIONS:
        return []
    faults = []
    elements = data.get("element") or []
    seen = set()
    for n, element in enumerate(elements):
        if class_name == "Set" and element in seen:
            faults.append(f"/element/{n}")
        seen.add(element)
    if class_name == "List":
        by_index, faults_of_order = _list_items(data)
        items = list(by_index.values())
    else:
        items = [(item, f"/item/{n}") for n, item in enumerate(data.get("item") or [])]
    count = len(items) if class_name in ("Bag", "List") else len(elements)
    if "co_size" in data and data["co_size"] != count:
        faults.append("/co_size")
    if "element" in data:
        faults += [
            f"{at}/itemContent"
            for item, at in items
            if item["itemContent"] not in elements
        ]
    if class_name == "List":
        faults += faults_of_order + _list_faults(data, by_index)
    return faults


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_examples_keep_the_rules_no_validator_checks(filepath):
    """Every valid example keeps CO's rules that no validator checks."""
    data = yaml.safe_load(Path(filepath).read_text())
    assert rule_faults(_class(filepath), data) == []


@pytest.mark.parametrize("filepath", RULE_EXAMPLE_FILES)
def test_rule_counter_examples_break_one_rule(filepath):
    """Each counter-example in problem/invalid passes the validator, which
    cannot check its rule, and breaks that rule at the place its first line
    names, and only there. Should the validator come to check a rule, the
    first assertion fails and the file moves to invalid/."""
    data = yaml.safe_load(Path(filepath).read_text())
    report = validate(data, str(SCHEMA), _class(filepath))
    assert not report.results, [r.message for r in report.results]
    assert set(rule_faults(_class(filepath), data)) == {_fails_at(filepath)}
