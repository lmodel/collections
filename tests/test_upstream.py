"""Hold the schema to the Collections Ontology's own file, offline.

src/collections/schema/upstream/collections.owl is CO 2.0's OWL file, copied
unchanged. These tests check that the copy is the pinned file, that the
schema header and the upstream watch name the same edition, and that the
schema renders every class and property of CO, by CO's name and IRI, with
the domains, ranges, cardinalities and class axioms CO states.
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

# CO's local names that the schema renders under another name, as lmodel/uco's
# uco_co module does, because UCO defines an Item and a size of its own.
RENAMED = {"Item": "CoItem", "size": "co_size"}


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


def test_cardinality_follows_co(view, co):
    """A functional object property, and a datatype property CO gives one value
    per class, is single-valued; every other object property is multivalued."""
    functional = set(co.subjects(RDF.type, OWL.FunctionalProperty))
    datatype = set(co.subjects(RDF.type, OWL.DatatypeProperty))
    for name, slot in view.all_slots().items():
        iri = _uri(view, slot)
        assert bool(slot.multivalued) == (iri not in functional | datatype), name


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
