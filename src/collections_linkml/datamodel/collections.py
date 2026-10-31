# Auto generated from collections.yaml by pythongen.py version: 0.0.1
# Schema: collections
#
# id: https://w3id.org/lmodel/collections
# description: The Collections Ontology (CO) 2.0 in LinkML, with CO's own names and IRIs: collections that are sets, bags or lists, and the items through which a bag or a list holds its elements.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.12.0"
version = "2.0"

# Namespaces
COLL = CurieNamespace('coll', 'http://purl.org/co/')
COLLECTIONS = CurieNamespace('collections', 'https://w3id.org/lmodel/collections/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = COLLECTIONS


# Types

# Class references



@dataclass(repr=False)
class Collection(YAMLRoot):
    """
    A group of things that is taken as a whole.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["Collection"]
    class_class_curie: ClassVar[str] = "coll:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.Collection

    co_size: Optional[int] = None
    element: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.co_size is not None and not isinstance(self.co_size, int):
            self.co_size = int(self.co_size)

        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.element]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Set(Collection):
    """
    A collection that holds each of its elements once.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["Set"]
    class_class_curie: ClassVar[str] = "coll:Set"
    class_name: ClassVar[str] = "Set"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.Set

    element: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.element]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bag(Collection):
    """
    A collection that may hold one element more than once, in no order.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["Bag"]
    class_class_curie: ClassVar[str] = "coll:Bag"
    class_name: ClassVar[str] = "Bag"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.Bag

    item: Optional[Union[Union[dict, "CoItem"], list[Union[dict, "CoItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="item", slot_type=CoItem, key_name="itemContent", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class List(Bag):
    """
    A collection whose items come in order, one after another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["List"]
    class_class_curie: ClassVar[str] = "coll:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.List

    firstItem: Optional[Union[dict, "ListItem"]] = None
    lastItem: Optional[Union[dict, "ListItem"]] = None
    item: Optional[Union[Union[dict, "ListItem"], list[Union[dict, "ListItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.firstItem is not None and not isinstance(self.firstItem, ListItem):
            self.firstItem = ListItem(**as_dict(self.firstItem))

        if self.lastItem is not None and not isinstance(self.lastItem, ListItem):
            self.lastItem = ListItem(**as_dict(self.lastItem))

        self._normalize_inlined_as_list(slot_name="item", slot_type=ListItem, key_name="itemContent", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoItem(YAMLRoot):
    """
    An entry of a bag, which wraps one of the bag's elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["Item"]
    class_class_curie: ClassVar[str] = "coll:Item"
    class_name: ClassVar[str] = "CoItem"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.CoItem

    itemContent: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.itemContent):
            self.MissingRequiredField("itemContent")
        if not isinstance(self.itemContent, URIorCURIE):
            self.itemContent = URIorCURIE(self.itemContent)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListItem(CoItem):
    """
    An item of a list, which has a place in the list's order.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COLL["ListItem"]
    class_class_curie: ClassVar[str] = "coll:ListItem"
    class_name: ClassVar[str] = "ListItem"
    class_model_uri: ClassVar[URIRef] = COLLECTIONS.ListItem

    itemContent: Union[str, URIorCURIE] = None
    index: int = None
    nextItem: Optional[Union[dict, "ListItem"]] = None
    previousItem: Optional[Union[dict, "ListItem"]] = None
    followedBy: Optional[Union[Union[dict, "ListItem"], list[Union[dict, "ListItem"]]]] = empty_list()
    precededBy: Optional[Union[Union[dict, "ListItem"], list[Union[dict, "ListItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.index):
            self.MissingRequiredField("index")
        if not isinstance(self.index, int):
            self.index = int(self.index)

        if self.nextItem is not None and not isinstance(self.nextItem, ListItem):
            self.nextItem = ListItem(**as_dict(self.nextItem))

        if self.previousItem is not None and not isinstance(self.previousItem, ListItem):
            self.previousItem = ListItem(**as_dict(self.previousItem))

        self._normalize_inlined_as_list(slot_name="followedBy", slot_type=ListItem, key_name="itemContent", keyed=False)

        self._normalize_inlined_as_list(slot_name="precededBy", slot_type=ListItem, key_name="itemContent", keyed=False)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.element = Slot(uri=COLL.element, name="element", curie=COLL.curie('element'),
                   model_uri=COLLECTIONS.element, domain=Collection, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.elementOf = Slot(uri=COLL.elementOf, name="elementOf", curie=COLL.curie('elementOf'),
                   model_uri=COLLECTIONS.elementOf, domain=None, range=Optional[Union[Union[dict, Collection], list[Union[dict, Collection]]]])

slots.co_size = Slot(uri=COLL.size, name="co_size", curie=COLL.curie('size'),
                   model_uri=COLLECTIONS.co_size, domain=Collection, range=Optional[int])

slots.item = Slot(uri=COLL.item, name="item", curie=COLL.curie('item'),
                   model_uri=COLLECTIONS.item, domain=Bag, range=Optional[Union[Union[dict, "CoItem"], list[Union[dict, "CoItem"]]]])

slots.itemOf = Slot(uri=COLL.itemOf, name="itemOf", curie=COLL.curie('itemOf'),
                   model_uri=COLLECTIONS.itemOf, domain=CoItem, range=Optional[Union[Union[dict, Bag], list[Union[dict, Bag]]]])

slots.itemContent = Slot(uri=COLL.itemContent, name="itemContent", curie=COLL.curie('itemContent'),
                   model_uri=COLLECTIONS.itemContent, domain=CoItem, range=Optional[Union[str, URIorCURIE]])

slots.itemContentOf = Slot(uri=COLL.itemContentOf, name="itemContentOf", curie=COLL.curie('itemContentOf'),
                   model_uri=COLLECTIONS.itemContentOf, domain=None, range=Optional[Union[Union[dict, CoItem], list[Union[dict, CoItem]]]])

slots.index = Slot(uri=COLL.index, name="index", curie=COLL.curie('index'),
                   model_uri=COLLECTIONS.index, domain=ListItem, range=Optional[int])

slots.firstItem = Slot(uri=COLL.firstItem, name="firstItem", curie=COLL.curie('firstItem'),
                   model_uri=COLLECTIONS.firstItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.firstItemOf = Slot(uri=COLL.firstItemOf, name="firstItemOf", curie=COLL.curie('firstItemOf'),
                   model_uri=COLLECTIONS.firstItemOf, domain=ListItem, range=Optional[Union[Union[dict, List], list[Union[dict, List]]]])

slots.lastItem = Slot(uri=COLL.lastItem, name="lastItem", curie=COLL.curie('lastItem'),
                   model_uri=COLLECTIONS.lastItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.lastItemOf = Slot(uri=COLL.lastItemOf, name="lastItemOf", curie=COLL.curie('lastItemOf'),
                   model_uri=COLLECTIONS.lastItemOf, domain=ListItem, range=Optional[Union[Union[dict, List], list[Union[dict, List]]]])

slots.nextItem = Slot(uri=COLL.nextItem, name="nextItem", curie=COLL.curie('nextItem'),
                   model_uri=COLLECTIONS.nextItem, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.previousItem = Slot(uri=COLL.previousItem, name="previousItem", curie=COLL.curie('previousItem'),
                   model_uri=COLLECTIONS.previousItem, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.followedBy = Slot(uri=COLL.followedBy, name="followedBy", curie=COLL.curie('followedBy'),
                   model_uri=COLLECTIONS.followedBy, domain=ListItem, range=Optional[Union[Union[dict, "ListItem"], list[Union[dict, "ListItem"]]]])

slots.precededBy = Slot(uri=COLL.precededBy, name="precededBy", curie=COLL.curie('precededBy'),
                   model_uri=COLLECTIONS.precededBy, domain=ListItem, range=Optional[Union[Union[dict, "ListItem"], list[Union[dict, "ListItem"]]]])

slots.Set_element = Slot(uri=COLL.element, name="Set_element", curie=COLL.curie('element'),
                   model_uri=COLLECTIONS.Set_element, domain=Set, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.List_item = Slot(uri=COLL.item, name="List_item", curie=COLL.curie('item'),
                   model_uri=COLLECTIONS.List_item, domain=List, range=Optional[Union[Union[dict, "ListItem"], list[Union[dict, "ListItem"]]]])

slots.CoItem_itemContent = Slot(uri=COLL.itemContent, name="CoItem_itemContent", curie=COLL.curie('itemContent'),
                   model_uri=COLLECTIONS.CoItem_itemContent, domain=CoItem, range=Union[str, URIorCURIE])

slots.ListItem_index = Slot(uri=COLL.index, name="ListItem_index", curie=COLL.curie('index'),
                   model_uri=COLLECTIONS.ListItem_index, domain=ListItem, range=int)
