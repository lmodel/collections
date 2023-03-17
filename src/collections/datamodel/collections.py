# Auto generated from collections.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-17T20:56:44
# Schema: collections
#
# id: https://w3id.org/lmodel/collections
# description: The Collections Ontology (CO) in Linkml
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer

metamodel_version = "1.7.0"
version = "2.0.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AFC = CurieNamespace('AFC', 'http://purl.allotrope.org/ontologies/common#AFC_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
SIO = CurieNamespace('SIO', 'http://identifiers.org/sio/')
CO = CurieNamespace('co', 'http://purl.org/co/')
COLLECTIONS = CurieNamespace('collections', 'https://w3id.org/lmodel/collections/')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPAR = CurieNamespace('spar', 'http://purl.org/spar/error')
SUMO = CurieNamespace('sumo', 'http://example.org/UNKNOWN/sumo/')
WIKIDATA = CurieNamespace('wikidata', 'http://identifiers.org/wikidata/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = COLLECTIONS


# Types
class PositiveInteger(Integer):
    """ integer greater than zero; natural number explicitly excluding zero """
    type_class_uri = XSD.positiveInteger
    type_class_curie = "xsd:positiveInteger"
    type_name = "positive integer"
    type_model_uri = COLLECTIONS.PositiveInteger


# Class references



class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Thing
    class_class_curie: ClassVar[str] = "collections:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.Thing


@dataclass
class Collection(Thing):
    """
    A group of objects that can be considered as a whole.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Collection
    class_class_curie: ClassVar[str] = "collections:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.Collection

    element: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    size: Optional[Union[int, PositiveInteger]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.element]

        if self.size is not None and not isinstance(self.size, PositiveInteger):
            self.size = PositiveInteger(self.size)

        super().__post_init__(**kwargs)


class Bag(Collection):
    """
    Collection that can have a number of copies of each object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Bag
    class_class_curie: ClassVar[str] = "collections:Bag"
    class_name: ClassVar[str] = "Bag"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.Bag


@dataclass
class CoItem(Thing):
    """
    Element belonging to a bag
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.CoItem
    class_class_curie: ClassVar[str] = "collections:CoItem"
    class_name: ClassVar[str] = "CoItem"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.CoItem

    itemOf: Optional[Union[dict, Bag]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.itemOf is not None and not isinstance(self.itemOf, Bag):
            self.itemOf = Bag(**as_dict(self.itemOf))

        super().__post_init__(**kwargs)


@dataclass
class List(Bag):
    """
    An ordered array of items, that can be present in multiple copies
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.List
    class_class_curie: ClassVar[str] = "collections:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.List

    item: Optional[Union[Union[dict, "ListItem"], List[Union[dict, "ListItem"]]]] = empty_list()
    lastItem: Optional[Union[dict, "ListItem"]] = None
    firstItem: Optional[Union[dict, "ListItem"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="item", slot_type=ListItem, key_name="_index", keyed=False)

        if self.lastItem is not None and not isinstance(self.lastItem, ListItem):
            self.lastItem = ListItem(**as_dict(self.lastItem))

        if self.firstItem is not None and not isinstance(self.firstItem, ListItem):
            self.firstItem = ListItem(**as_dict(self.firstItem))

        super().__post_init__(**kwargs)


@dataclass
class ListItem(CoItem):
    """
    element belonging to a list
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.ListItem
    class_class_curie: ClassVar[str] = "collections:ListItem"
    class_name: ClassVar[str] = "ListItem"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.ListItem

    _index: Union[int, PositiveInteger] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self._index):
            self.MissingRequiredField("_index")
        if not isinstance(self._index, PositiveInteger):
            self._index = PositiveInteger(self._index)

        super().__post_init__(**kwargs)


class Set(Collection):
    """
    A collection that cannot contain duplicate elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Set
    class_class_curie: ClassVar[str] = "collections:Set"
    class_name: ClassVar[str] = "Set"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.Set


# Enumerations


# Slots
class slots:
    pass

slots.element = Slot(uri=COLLECTIONS.element, name="element", curie=COLLECTIONS.curie('element'),
                   model_uri=COLLECTIONS.element, domain=Collection, range=Optional[Union[dict, "Thing"]])

slots.elementOf = Slot(uri=COLLECTIONS.elementOf, name="elementOf", curie=COLLECTIONS.curie('elementOf'),
                   model_uri=COLLECTIONS.elementOf, domain=Thing, range=Optional[Union[dict, Collection]])

slots.firstItem = Slot(uri=COLLECTIONS.firstItem, name="firstItem", curie=COLLECTIONS.curie('firstItem'),
                   model_uri=COLLECTIONS.firstItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.firstItemOf = Slot(uri=COLLECTIONS.firstItemOf, name="firstItemOf", curie=COLLECTIONS.curie('firstItemOf'),
                   model_uri=COLLECTIONS.firstItemOf, domain=ListItem, range=Optional[Union[dict, List]])

slots.followedBy = Slot(uri=COLLECTIONS.followedBy, name="followedBy", curie=COLLECTIONS.curie('followedBy'),
                   model_uri=COLLECTIONS.followedBy, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.item = Slot(uri=COLLECTIONS.item, name="item", curie=COLLECTIONS.curie('item'),
                   model_uri=COLLECTIONS.item, domain=Bag, range=Optional[Union[dict, "CoItem"]])

slots.itemContent = Slot(uri=COLLECTIONS.itemContent, name="itemContent", curie=COLLECTIONS.curie('itemContent'),
                   model_uri=COLLECTIONS.itemContent, domain=CoItem, range=Optional[Union[dict, "CoItem"]])

slots.itemContentOf = Slot(uri=COLLECTIONS.itemContentOf, name="itemContentOf", curie=COLLECTIONS.curie('itemContentOf'),
                   model_uri=COLLECTIONS.itemContentOf, domain=CoItem, range=Optional[Union[dict, CoItem]])

slots.itemOf = Slot(uri=COLLECTIONS.itemOf, name="itemOf", curie=COLLECTIONS.curie('itemOf'),
                   model_uri=COLLECTIONS.itemOf, domain=CoItem, range=Optional[Union[dict, Bag]])

slots.lastItem = Slot(uri=COLLECTIONS.lastItem, name="lastItem", curie=COLLECTIONS.curie('lastItem'),
                   model_uri=COLLECTIONS.lastItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.lastItemOf = Slot(uri=COLLECTIONS.lastItemOf, name="lastItemOf", curie=COLLECTIONS.curie('lastItemOf'),
                   model_uri=COLLECTIONS.lastItemOf, domain=ListItem, range=Optional[Union[dict, List]])

slots.nextItem = Slot(uri=COLLECTIONS.nextItem, name="nextItem", curie=COLLECTIONS.curie('nextItem'),
                   model_uri=COLLECTIONS.nextItem, domain=Thing, range=Optional[Union[dict, ListItem]])

slots.precededBy = Slot(uri=COLLECTIONS.precededBy, name="precededBy", curie=COLLECTIONS.curie('precededBy'),
                   model_uri=COLLECTIONS.precededBy, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.previousItem = Slot(uri=COLLECTIONS.previousItem, name="previousItem", curie=COLLECTIONS.curie('previousItem'),
                   model_uri=COLLECTIONS.previousItem, domain=ListItem, range=Optional[Union[dict, "Thing"]])

slots._index = Slot(uri=COLLECTIONS._index, name="_index", curie=COLLECTIONS.curie('_index'),
                   model_uri=COLLECTIONS._index, domain=ListItem, range=Optional[Union[int, PositiveInteger]])

slots.size = Slot(uri=COLLECTIONS.size, name="size", curie=COLLECTIONS.curie('size'),
                   model_uri=COLLECTIONS.size, domain=Collection, range=Optional[Union[int, PositiveInteger]])

slots.Collection_element = Slot(uri=COLLECTIONS.element, name="Collection_element", curie=COLLECTIONS.curie('element'),
                   model_uri=COLLECTIONS.Collection_element, domain=Collection, range=Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]])

slots.Collection_size = Slot(uri=COLLECTIONS.size, name="Collection_size", curie=COLLECTIONS.curie('size'),
                   model_uri=COLLECTIONS.Collection_size, domain=Collection, range=Optional[Union[int, PositiveInteger]])

slots.List_lastItem = Slot(uri=COLLECTIONS.lastItem, name="List_lastItem", curie=COLLECTIONS.curie('lastItem'),
                   model_uri=COLLECTIONS.List_lastItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.List_firstItem = Slot(uri=COLLECTIONS.firstItem, name="List_firstItem", curie=COLLECTIONS.curie('firstItem'),
                   model_uri=COLLECTIONS.List_firstItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.List_item = Slot(uri=COLLECTIONS.item, name="List_item", curie=COLLECTIONS.curie('item'),
                   model_uri=COLLECTIONS.List_item, domain=List, range=Optional[Union[Union[dict, "ListItem"], List[Union[dict, "ListItem"]]]])

slots.ListItem__index = Slot(uri=COLLECTIONS._index, name="ListItem__index", curie=COLLECTIONS.curie('_index'),
                   model_uri=COLLECTIONS.ListItem__index, domain=ListItem, range=Union[int, PositiveInteger])