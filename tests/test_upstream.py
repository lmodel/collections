"""Hold the schema to the Collections Ontology's own file, offline.

src/collections/schema/upstream/collections.owl is CO 2.0's OWL file, copied
unchanged. These tests check that the copy is the pinned file, that the
schema header and the upstream watch name the same edition, and that the
schema renders every class and property of CO, by CO's name and IRI, with
the domains, ranges, cardinalities, required slots and class axioms CO
states.
"""

import hashlib
import importlib.util
from pathlib import Path

import pytest
import rdflib
import yaml
from linkml_runtime.utils.schemaview import SchemaView
from rdflib.namespace import OWL, RDF, RDFS

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "collections" / "schema" / "collections.yaml"
COPY = ROOT / "src" / "collections" / "schema" / "upstream" / "collections.owl"
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
CO = rdflib.Namespace("http://purl.org/co/")

# CO's local names that the schema renders under another name: Item and size,
# as lmodel/uco's uco_co module does, because UCO defines an Item and a size
# of its own, and index, because gen-doc writes the page of a slot named index
# over the schema's index page.
RENAMED = {"Item": "CoItem", "size": "co_size", "index": "co_index"}

# Where the schema's required slots depart from CO's class restrictions. CO
# gives every collection exactly one size, which the schema leaves optional,
# since a reader can count and the tests check a size where it is given. CO's
# OWL file lets an item wrap at most one resource, and its wiki page
# StructureBag says exactly one, so the schema requires an item's content.
OPTIONAL_HERE = {CO.size}
REQUIRED_BY_THE_WIKI = {CO.Item: {CO.itemContent}}


@pytest.fixture(scope="module")
def watch():
    spec = importlib.util.spec_from_file_location("watch_pins", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def co():
    graph = rdflib.Graph()
    graph.parse(COPY, format="xml")
    return graph


@pytest.fixture(scope="module")
def view():
    return SchemaView(str(SCHEMA))


def _co_terms(co, kinds):
    return {
        s for kind in kinds for s in co.subjects(RDF.type, kind) if s.startswith(CO)
    }


def _local(iri):
    return str(iri).removeprefix(str(CO))


def _uri(view, element):
    """The IRI the schema gives a class or a slot."""
    curie = getattr(element, "class_uri", None) or element.slot_uri
    return rdflib.URIRef(view.expand_curie(curie))


def test_the_copy_is_the_pinned_file(watch):
    """The copy's git object hash is the one the watch pins."""
    data = COPY.read_bytes()
    assert (
        hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest() == watch.PINNED_BLOB
    )


def test_the_header_names_the_pinned_edition(watch, co):
    """The header's version, source and annotations, the watch's pins and the
    copy's owl:versionInfo agree."""
    header = yaml.safe_load(SCHEMA.read_text())
    assert header["version"] == watch.PINNED_EDITION
    assert header["source"] == watch.PINNED_SOURCE
    assert header["annotations"]["co_commit"] == watch.PINNED_COMMIT
    assert header["annotations"]["co_git_object"] == watch.PINNED_BLOB
    ontology = rdflib.URIRef(header["annotations"]["co_ontology_iri"])
    assert (ontology, RDF.type, OWL.Ontology) in co
    assert [str(v) for v in co.objects(ontology, OWL.versionInfo)] == [
        watch.PINNED_EDITION
    ]


def test_every_class_of_co_is_rendered_by_its_name(view, co):
    classes = {_uri(view, c): name for name, c in view.all_classes().items()}
    assert set(classes) == _co_terms(co, [OWL.Class])
    for iri, name in classes.items():
        assert name == RENAMED.get(_local(iri), _local(iri))


def test_every_property_of_co_is_rendered_by_its_name(view, co):
    slots = {_uri(view, s): name for name, s in view.all_slots().items()}
    assert set(slots) == _co_terms(co, [OWL.ObjectProperty, OWL.DatatypeProperty])
    for iri, name in slots.items():
        assert name == RENAMED.get(_local(iri), _local(iri))


def _named(co, node):
    """The CO classes a class expression names: itself, or the members of an
    intersection."""
    if isinstance(node, rdflib.URIRef):
        return {node}
    members = co.value(node, OWL.intersectionOf)
    if members is None:
        return set()
    return {
        m
        for m in rdflib.collection.Collection(co, members)
        if isinstance(m, rdflib.URIRef)
    }


def test_domains_and_ranges_follow_co(view, co):
    """Where CO states a property's domain or range, the slot has it: a
    class, or the bounds of an XSD integer type."""
    xsd = rdflib.namespace.XSD
    bounds = {xsd.positiveInteger: 1, xsd.nonNegativeInteger: 0}
    for name, slot in view.all_slots().items():
        iri = _uri(view, slot)
        for domain in co.objects(iri, RDFS.domain):
            assert _uri(view, view.get_class(slot.domain)) in _named(co, domain), name
        for rng in co.objects(iri, RDFS.range):
            if rng in bounds:
                assert (slot.range, slot.minimum_value) == ("integer", bounds[rng]), (
                    name
                )
            elif _named(co, rng):
                assert _uri(view, view.get_class(slot.range)) in _named(co, rng), name
            else:
                # itemContent ranges over anything that is not an item.
                assert slot.range == "uriorcurie", name


def _restrictions(co, cls):
    """The named classes a CO class is, itself and its superclasses, and the
    restrictions they state on a named property, each as the property with
    the least and the most number of values it allows (None for no bound)."""
    classes, found, todo, seen = set(), [], [cls], set()
    while todo:
        node = todo.pop()
        if node in seen:
            continue
        seen.add(node)
        if isinstance(node, rdflib.URIRef):
            classes.add(node)
        todo += co.objects(node, RDFS.subClassOf)
        members = co.value(node, OWL.intersectionOf)
        if members is not None:
            todo += rdflib.collection.Collection(co, members)
        prop = co.value(node, OWL.onProperty)
        if not isinstance(prop, rdflib.URIRef):
            continue
        exact = co.value(node, OWL.cardinality)
        least = exact if exact is not None else co.value(node, OWL.minCardinality)
        most = exact if exact is not None else co.value(node, OWL.maxCardinality)
        if co.value(node, OWL.someValuesFrom) is not None:
            least = 1
        found.append(
            (
                prop,
                None if least is None else int(least),
                None if most is None else int(most),
            )
        )
    return classes, found


def test_cardinality_follows_co(view, co):
    """A slot is single-valued where CO makes its property functional or a
    class restriction allows it one value at most, and multivalued
    otherwise."""
    single = set(co.subjects(RDF.type, OWL.FunctionalProperty))
    for cls in view.all_classes().values():
        _, restrictions = _restrictions(co, _uri(view, cls))
        single |= {p for p, _, most in restrictions if most is not None and most <= 1}
    for name, slot in view.all_slots().items():
        assert bool(slot.multivalued) == (_uri(view, slot) not in single), name


def test_required_slots_follow_co(view, co):
    """A class requires the slots whose properties CO's restrictions give it at
    least one value of, but for the departures listed above."""
    for name, cls in view.all_classes().items():
        classes, restrictions = _restrictions(co, _uri(view, cls))
        expected = {p for p, least, _ in restrictions if least}
        for owner, props in REQUIRED_BY_THE_WIKI.items():
            if owner in classes:
                expected |= props
        required = {_uri(view, s) for s in view.class_induced_slots(name) if s.required}
        assert required == expected - OPTIONAL_HERE, name


def test_inverses_and_transitivity_follow_co(view, co):
    """Every inverse the schema states is one CO declares, and the transitive
    slots are CO's transitive properties."""
    inverses = {frozenset(p) for p in co.subject_objects(OWL.inverseOf)}
    for name, slot in view.all_slots().items():
        if slot.inverse:
            pair = {_uri(view, slot), _uri(view, view.get_slot(slot.inverse))}
            assert frozenset(pair) in inverses, name
    transitive = {_uri(view, s) for s in view.all_slots().values() if s.transitive}
    assert transitive == set(co.subjects(RDF.type, OWL.TransitiveProperty))


def test_class_axioms_follow_co(view, co):
    """Each class's parent is a superclass CO names, and the disjoint pairs
    are CO's."""
    for name, cls in view.all_classes().items():
        if cls.is_a:
            parent = _uri(view, view.get_class(cls.is_a))
            named = set().union(
                *(_named(co, s) for s in co.objects(_uri(view, cls), RDFS.subClassOf))
            )
            assert parent in named, name
    stated = {
        frozenset({_uri(view, cls), _uri(view, view.get_class(other))})
        for cls in view.all_classes().values()
        for other in cls.disjoint_with
    }
    assert stated == {frozenset(p) for p in co.subject_objects(OWL.disjointWith)}
