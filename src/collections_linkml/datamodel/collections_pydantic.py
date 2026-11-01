from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "2.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'co_commit': {'tag': 'co_commit',
                                   'value': '619e7b02646321174635fd04be658e338bf7d1d7'},
                     'co_git_object': {'tag': 'co_git_object',
                                       'value': '4e19e4892212de2b1805923a7a69fa4ba8c1b424'},
                     'co_licence': {'tag': 'co_licence',
                                    'value': 'Apache-2.0 for code, collections.owl '
                                             'among it, and CC-BY-3.0 for other '
                                             'content, per the Google Code '
                                             'archive'},
                     'co_ontology_iri': {'tag': 'co_ontology_iri',
                                         'value': 'http://purl.org/co'}},
     'comments': ['Renders CO 2.0 by Paolo Ciccarese and Silvio Peroni, whose '
                  'ontology IRI is http://purl.org/co. The source is '
                  'collections.owl at the commit the co_commit annotation names, '
                  'copied unchanged to upstream/collections.owl.',
                  "The repository states no licence. The project's Google Code "
                  'archive gives the Apache License 2.0 for its code, '
                  'collections.owl among it, and CC BY 3.0 for its other content, '
                  'such as its wiki, as the co_licence annotation says. The '
                  "descriptions here are this project's own words.",
                  'Items have no IRI here, so a slot that links to an item, such '
                  'as firstItem or nextItem, holds a copy of that item. '
                  'docs/index.md lists the rules of CO that no validator checks '
                  'and the tests check instead.',
                  'The exact, narrow and broad mappings to SWAN Collections 1.2, '
                  'the ontologydesignpatterns.org patterns, the Music Ontology and '
                  "OAI-ORE are those of CO's own alignment.owl, copied unchanged "
                  "to upstream/alignment.owl. That file writes ORE's namespace as "
                  'http://www.openarchives.org/ore/items/, where ORE defines its '
                  'terms under http://www.openarchives.org/ore/terms/, which the '
                  "mappings use. The mappings to schema.org are this project's "
                  "own, after schema.org's ItemList and ListItem, which link list "
                  'items the same way.'],
     'default_prefix': 'collections',
     'default_range': 'string',
     'description': "The Collections Ontology (CO) 2.0 in LinkML, with CO's own "
                    'names and IRIs: collections that are sets, bags or lists, and '
                    'the items through which a bag or a list holds its elements.',
     'id': 'https://w3id.org/lmodel/collections',
     'imports': ['linkml:types'],
     'in_language': 'en',
     'keywords': ['collection', 'set', 'bag', 'list', 'ordered list'],
     'license': 'Apache-2.0',
     'name': 'collections',
     'notes': ["CO's Item and size are named CoItem and co_size, as in "
               "lmodel/uco's uco_co module, because UCO defines an Item and a size "
               "of its own. CO's index is named co_index, because gen-doc writes "
               "the page of a slot named index over the schema's index page. Their "
               "IRIs are CO's."],
     'prefixes': {'coll': {'prefix_prefix': 'coll',
                           'prefix_reference': 'http://purl.org/co/'},
                  'collections': {'prefix_prefix': 'collections',
                                  'prefix_reference': 'https://w3id.org/lmodel/collections/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mo': {'prefix_prefix': 'mo',
                         'prefix_reference': 'http://purl.org/ontology/mo/'},
                  'odpbag': {'prefix_prefix': 'odpbag',
                             'prefix_reference': 'http://www.ontologydesignpatterns.org/cp/owl/bag.owl#'},
                  'odpce': {'prefix_prefix': 'odpce',
                            'prefix_reference': 'http://www.ontologydesignpatterns.org/cp/owl/collectionentity.owl#'},
                  'odplist': {'prefix_prefix': 'odplist',
                              'prefix_reference': 'http://www.ontologydesignpatterns.org/cp/owl/list.owl#'},
                  'odpset': {'prefix_prefix': 'odpset',
                             'prefix_reference': 'http://www.ontologydesignpatterns.org/cp/owl/set.owl#'},
                  'ore': {'prefix_prefix': 'ore',
                          'prefix_reference': 'http://www.openarchives.org/ore/terms/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'seq': {'prefix_prefix': 'seq',
                          'prefix_reference': 'http://www.ontologydesignpatterns.org/cp/owl/sequence.owl#'},
                  'swan': {'prefix_prefix': 'swan',
                           'prefix_reference': 'http://swan.mindinformatics.org/ontologies/1.2/collections/'}},
     'see_also': ['https://lmodel.github.io/collections',
                  'https://doi.org/10.3233/SW-130121'],
     'source': 'https://github.com/collections-ontology/collections-ontology',
     'source_file': 'src/collections/schema/collections.yaml',
     'title': 'Collections Ontology (CO)'} )


class Collection(ConfiguredBaseModel):
    """
    A group of things that is taken as a whole.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'children_are_mutually_disjoint': True,
         'class_uri': 'coll:Collection',
         'comments': ['Its children are marked mutually disjoint because gen-owl drops '
                      'disjoint_with (linkml issue 3950), so this is how the generated '
                      'ontology states that a set is never a bag.'],
         'disjoint_with': ['CoItem'],
         'exact_mappings': ['swan:Collection', 'odpce:Collection'],
         'from_schema': 'https://w3id.org/lmodel/collections',
         'narrow_mappings': ['ore:Aggregation']})

    co_size: Optional[int] = Field(default=None, description="""How many times the collection holds a thing, counting each repeat: the number of elements of a set, or of items of a bag or a list.""", ge=0, json_schema_extra = { "linkml_meta": {'aliases': ['size'],
         'domain': 'Collection',
         'domain_of': ['Collection'],
         'exact_mappings': ['swan:size', 'odpbag:size', 'odpset:size'],
         'narrow_mappings': ['mo:track_count', 'schema:numberOfItems'],
         'notes': ['CO gives every collection exactly one size. The schema leaves it '
                   'optional, since a reader can count; where it is given, the tests '
                   'check that it equals the count.'],
         'slot_uri': 'coll:size'} })
    element: Optional[list[str]] = Field(default=None, description="""A thing the collection holds, named by its IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["In a bag, each item's itemContent is also an element, as the "
                      "path rule states after CO's property chain."],
         'domain': 'Collection',
         'domain_of': ['Collection'],
         'narrow_mappings': ['swan:element', 'odpce:hasMember', 'ore:aggregates'],
         'path_rule': {'followed_by': {'traverse': 'itemContent'}, 'traverse': 'item'},
         'slot_uri': 'coll:element'} })


class Set(Collection):
    """
    A collection that holds each of its elements once.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'coll:Set',
         'comments': ["No validator checks that the elements differ: LinkML 1.12.1's "
                      'generators drop list_elements_unique, so the tests check it.'],
         'exact_mappings': ['swan:Set', 'odpset:Set'],
         'from_schema': 'https://w3id.org/lmodel/collections',
         'slot_usage': {'element': {'list_elements_unique': True, 'name': 'element'}}})

    co_size: Optional[int] = Field(default=None, description="""How many times the collection holds a thing, counting each repeat: the number of elements of a set, or of items of a bag or a list.""", ge=0, json_schema_extra = { "linkml_meta": {'aliases': ['size'],
         'domain': 'Collection',
         'domain_of': ['Collection'],
         'exact_mappings': ['swan:size', 'odpbag:size', 'odpset:size'],
         'narrow_mappings': ['mo:track_count', 'schema:numberOfItems'],
         'notes': ['CO gives every collection exactly one size. The schema leaves it '
                   'optional, since a reader can count; where it is given, the tests '
                   'check that it equals the count.'],
         'slot_uri': 'coll:size'} })
    element: Optional[list[str]] = Field(default=None, description="""A thing the collection holds, named by its IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["In a bag, each item's itemContent is also an element, as the "
                      "path rule states after CO's property chain."],
         'domain': 'Collection',
         'domain_of': ['Collection'],
         'list_elements_unique': True,
         'narrow_mappings': ['swan:element', 'odpce:hasMember', 'ore:aggregates'],
         'path_rule': {'followed_by': {'traverse': 'itemContent'}, 'traverse': 'item'},
         'slot_uri': 'coll:element'} })


class Bag(Collection):
    """
    A collection that may hold one element more than once, in no order.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'coll:Bag',
         'disjoint_with': ['Set'],
         'exact_mappings': ['swan:Bag', 'odpbag:Bag'],
         'from_schema': 'https://w3id.org/lmodel/collections'})

    item: Optional[list[CoItem]] = Field(default=None, description="""An item of the bag, which holds one of its elements.""", json_schema_extra = { "linkml_meta": {'comments': ['In a list, the item after an item of the list is also an item '
                      "of it, as the path rule states after CO's property chain."],
         'domain': 'Bag',
         'domain_of': ['Bag'],
         'narrow_mappings': ['swan:item', 'mo:track'],
         'path_rule': {'followed_by': {'traverse': 'nextItem'}, 'traverse': 'item'},
         'slot_uri': 'coll:item'} })
    co_size: Optional[int] = Field(default=None, description="""How many times the collection holds a thing, counting each repeat: the number of elements of a set, or of items of a bag or a list.""", ge=0, json_schema_extra = { "linkml_meta": {'aliases': ['size'],
         'domain': 'Collection',
         'domain_of': ['Collection'],
         'exact_mappings': ['swan:size', 'odpbag:size', 'odpset:size'],
         'narrow_mappings': ['mo:track_count', 'schema:numberOfItems'],
         'notes': ['CO gives every collection exactly one size. The schema leaves it '
                   'optional, since a reader can count; where it is given, the tests '
                   'check that it equals the count.'],
         'slot_uri': 'coll:size'} })
    element: Optional[list[str]] = Field(default=None, description="""A thing the collection holds, named by its IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["In a bag, each item's itemContent is also an element, as the "
                      "path rule states after CO's property chain."],
         'domain': 'Collection',
         'domain_of': ['Collection'],
         'narrow_mappings': ['swan:element', 'odpce:hasMember', 'ore:aggregates'],
         'path_rule': {'followed_by': {'traverse': 'itemContent'}, 'traverse': 'item'},
         'slot_uri': 'coll:element'} })


class List(Bag):
    """
    A collection whose items come in order, one after another.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['schema:ItemList'],
         'class_uri': 'coll:List',
         'comments': ['No validator checks the order: that the indexes count from 1 '
                      'with no gap or repeat, and that firstItem, lastItem and each '
                      "item's links agree with them. The tests check it."],
         'exact_mappings': ['swan:List', 'odplist:List'],
         'from_schema': 'https://w3id.org/lmodel/collections',
         'narrow_mappings': ['mo:Record'],
         'slot_usage': {'item': {'name': 'item', 'range': 'ListItem'}}})

    firstItem: Optional[ListItem] = Field(default=None, description="""The first item of the list.""", json_schema_extra = { "linkml_meta": {'comments': ['It holds a copy of the item with index 1, which has no previous '
                      'item.'],
         'domain': 'List',
         'domain_of': ['List'],
         'narrow_mappings': ['swan:firstItem'],
         'notes': ['CO makes it a narrower form of item, which is not stated here. '
                   "LinkML's inheritance is monotonic, so a slot under item would be "
                   'multivalued, as item is, and this one holds one item.'],
         'slot_uri': 'coll:firstItem'} })
    lastItem: Optional[ListItem] = Field(default=None, description="""The last item of the list.""", json_schema_extra = { "linkml_meta": {'comments': ['It holds a copy of the item with the highest index, which has '
                      'no next item.'],
         'domain': 'List',
         'domain_of': ['List'],
         'narrow_mappings': ['swan:lastItem'],
         'notes': ['CO makes it a narrower form of item, which is not stated here for '
                   'the reason given on firstItem.'],
         'slot_uri': 'coll:lastItem'} })
    item: Optional[list[ListItem]] = Field(default=None, description="""An item of the bag, which holds one of its elements.""", json_schema_extra = { "linkml_meta": {'comments': ['In a list, the item after an item of the list is also an item '
                      "of it, as the path rule states after CO's property chain."],
         'domain': 'Bag',
         'domain_of': ['Bag'],
         'narrow_mappings': ['swan:item', 'mo:track'],
         'path_rule': {'followed_by': {'traverse': 'nextItem'}, 'traverse': 'item'},
         'slot_uri': 'coll:item'} })
    co_size: Optional[int] = Field(default=None, description="""How many times the collection holds a thing, counting each repeat: the number of elements of a set, or of items of a bag or a list.""", ge=0, json_schema_extra = { "linkml_meta": {'aliases': ['size'],
         'domain': 'Collection',
         'domain_of': ['Collection'],
         'exact_mappings': ['swan:size', 'odpbag:size', 'odpset:size'],
         'narrow_mappings': ['mo:track_count', 'schema:numberOfItems'],
         'notes': ['CO gives every collection exactly one size. The schema leaves it '
                   'optional, since a reader can count; where it is given, the tests '
                   'check that it equals the count.'],
         'slot_uri': 'coll:size'} })
    element: Optional[list[str]] = Field(default=None, description="""A thing the collection holds, named by its IRI.""", json_schema_extra = { "linkml_meta": {'comments': ["In a bag, each item's itemContent is also an element, as the "
                      "path rule states after CO's property chain."],
         'domain': 'Collection',
         'domain_of': ['Collection'],
         'narrow_mappings': ['swan:element', 'odpce:hasMember', 'ore:aggregates'],
         'path_rule': {'followed_by': {'traverse': 'itemContent'}, 'traverse': 'item'},
         'slot_uri': 'coll:element'} })


class CoElement(ConfiguredBaseModel):
    """
    A thing that a collection holds, named by its IRI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['CO puts no limit on what a collection holds. A value of element '
                      'or itemContent is the IRI of a CoElement, so the RDF of a '
                      'collection links to its elements rather than holding their IRIs '
                      'as text.'],
         'disjoint_with': ['CoItem'],
         'from_schema': 'https://w3id.org/lmodel/collections',
         'notes': ["Not a term of CO, so its IRI is the schema's own. CO says that "
                   'what an item wraps is not itself an item, which disjoint_with '
                   'states.']})

    iri: str = Field(default=..., description="""The IRI of the thing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoElement']} })


class CoItem(ConfiguredBaseModel):
    """
    An entry of a bag, which wraps one of the bag's elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Item'],
         'class_uri': 'coll:Item',
         'exact_mappings': ['swan:Item', 'odpbag:Item'],
         'from_schema': 'https://w3id.org/lmodel/collections',
         'notes': ['CO says that every item is an item of some bag. The schema leaves '
                   'itemOf optional, since a bag holds its items inline.'],
         'slot_usage': {'itemContent': {'name': 'itemContent', 'required': True}}})

    itemContent: str = Field(default=..., description="""The element that the item wraps.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:item'],
         'domain': 'CoItem',
         'domain_of': ['CoItem'],
         'exact_mappings': ['swan:itemContent', 'odpbag:itemContent'],
         'narrow_mappings': ['mo:publication_of', 'ore:proxyFor'],
         'notes': ["CoItem requires it. CO's OWL file makes itemContent functional, so "
                   "an item wraps at most one element, and CO's wiki page StructureBag "
                   'says that an item links exactly one resource.'],
         'see_also': ['https://github.com/collections-ontology/collections-ontology/blob/58e55d956991878307d430eede7790d5e5da206f/StructureBag.md'],
         'slot_uri': 'coll:itemContent'} })


class ListItem(CoItem):
    """
    An item of a list, which has a place in the list's order.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'coll:ListItem',
         'close_mappings': ['schema:ListItem'],
         'exact_mappings': ['swan:ListItem', 'odplist:ListItem'],
         'from_schema': 'https://w3id.org/lmodel/collections',
         'narrow_mappings': ['mo:Track', 'ore:Proxy'],
         'slot_usage': {'co_index': {'name': 'co_index', 'required': True}}})

    co_index: int = Field(default=..., description="""The place of the item in its list, counting from 1.""", ge=1, json_schema_extra = { "linkml_meta": {'aliases': ['index'],
         'close_mappings': ['schema:position'],
         'domain': 'ListItem',
         'domain_of': ['ListItem'],
         'narrow_mappings': ['mo:track_number'],
         'slot_uri': 'coll:index'} })
    nextItem: Optional[ListItem] = Field(default=None, description="""The item that comes straight after this one.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:nextItem'],
         'comments': ['It holds a copy of the item whose index is one higher.'],
         'domain': 'ListItem',
         'domain_of': ['ListItem'],
         'exact_mappings': ['swan:nextItem'],
         'notes': ['CO makes it a narrower form of followedBy. It is stated on '
                   "followedBy, as transitive_form_of, not here as is_a: LinkML's "
                   'inheritance is monotonic, so a slot under followedBy would be '
                   'multivalued and transitive, as followedBy is, and this one is '
                   'neither.'],
         'slot_uri': 'coll:nextItem'} })
    previousItem: Optional[ListItem] = Field(default=None, description="""The item that comes straight before this one.""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['seq:directlyFollows'],
         'close_mappings': ['schema:previousItem'],
         'comments': ['It holds a copy of the item whose index is one lower.'],
         'domain': 'ListItem',
         'domain_of': ['ListItem'],
         'exact_mappings': ['swan:previousItem'],
         'inverse': 'nextItem',
         'notes': ['CO makes it a narrower form of precededBy. It is stated on '
                   'precededBy, as transitive_form_of, not here as is_a, for the '
                   'reason given on nextItem.'],
         'slot_uri': 'coll:previousItem'} })
    followedBy: Optional[list[ListItem]] = Field(default=None, description="""An item that comes somewhere after this one.""", json_schema_extra = { "linkml_meta": {'comments': ['It holds copies of items whose index is higher.'],
         'domain': 'ListItem',
         'domain_of': ['ListItem'],
         'exact_mappings': ['swan:followedBy'],
         'slot_uri': 'coll:followedBy',
         'transitive': True,
         'transitive_form_of': 'nextItem'} })
    precededBy: Optional[list[ListItem]] = Field(default=None, description="""An item that comes somewhere before this one.""", json_schema_extra = { "linkml_meta": {'comments': ['It holds copies of items whose index is lower.'],
         'domain': 'ListItem',
         'domain_of': ['ListItem'],
         'exact_mappings': ['swan:preceededBy'],
         'inverse': 'followedBy',
         'slot_uri': 'coll:precededBy',
         'transitive': True,
         'transitive_form_of': 'previousItem'} })
    itemContent: str = Field(default=..., description="""The element that the item wraps.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:item'],
         'domain': 'CoItem',
         'domain_of': ['CoItem'],
         'exact_mappings': ['swan:itemContent', 'odpbag:itemContent'],
         'narrow_mappings': ['mo:publication_of', 'ore:proxyFor'],
         'notes': ["CoItem requires it. CO's OWL file makes itemContent functional, so "
                   "an item wraps at most one element, and CO's wiki page StructureBag "
                   'says that an item links exactly one resource.'],
         'see_also': ['https://github.com/collections-ontology/collections-ontology/blob/58e55d956991878307d430eede7790d5e5da206f/StructureBag.md'],
         'slot_uri': 'coll:itemContent'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Collection.model_rebuild()
Set.model_rebuild()
Bag.model_rebuild()
List.model_rebuild()
CoElement.model_rebuild()
CoItem.model_rebuild()
ListItem.model_rebuild()
