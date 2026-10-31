-- # Class: Collection Description: A group of things that is taken as a whole.
--     * Slot: id
--     * Slot: co_size Description: How many times the collection holds a thing, counting each repeat: the number of elements of a set, or of items of a bag or a list.
-- # Class: Set Description: A collection that holds each of its elements once.
--     * Slot: id
--     * Slot: co_size Description: How many times the collection holds a thing, counting each repeat: the number of elements of a set, or of items of a bag or a list.
-- # Class: Bag Description: A collection that may hold one element more than once, in no order.
--     * Slot: id
--     * Slot: co_size Description: How many times the collection holds a thing, counting each repeat: the number of elements of a set, or of items of a bag or a list.
-- # Class: List Description: A collection whose items come in order, one after another.
--     * Slot: id
--     * Slot: co_size Description: How many times the collection holds a thing, counting each repeat: the number of elements of a set, or of items of a bag or a list.
--     * Slot: firstItem_id Description: The first item of the list.
--     * Slot: lastItem_id Description: The last item of the list.
-- # Class: CoElement Description: A thing that a collection holds, named by its IRI.
--     * Slot: iri Description: The IRI of the thing.
-- # Class: CoItem Description: An entry of a bag, which wraps one of the bag's elements.
--     * Slot: id
--     * Slot: itemContent Description: The element that the item wraps.
--     * Slot: Bag_id Description: Autocreated FK slot
-- # Class: ListItem Description: An item of a list, which has a place in the list's order.
--     * Slot: id
--     * Slot: co_index Description: The place of the item in its list, counting from 1.
--     * Slot: itemContent Description: The element that the item wraps.
--     * Slot: List_id Description: Autocreated FK slot
--     * Slot: ListItem_id Description: Autocreated FK slot
--     * Slot: nextItem_id Description: The item that comes straight after this one.
--     * Slot: previousItem_id Description: The item that comes straight before this one.
-- # Class: Collection_element
--     * Slot: Collection_id Description: Autocreated FK slot
--     * Slot: element_iri Description: A thing the collection holds, named by its IRI.
-- # Class: Set_element
--     * Slot: Set_id Description: Autocreated FK slot
--     * Slot: element_iri Description: A thing the collection holds, named by its IRI.
-- # Class: Bag_element
--     * Slot: Bag_id Description: Autocreated FK slot
--     * Slot: element_iri Description: A thing the collection holds, named by its IRI.
-- # Class: List_element
--     * Slot: List_id Description: Autocreated FK slot
--     * Slot: element_iri Description: A thing the collection holds, named by its IRI.

CREATE TABLE "Collection" (
	id INTEGER NOT NULL,
	co_size INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Collection_id" ON "Collection" (id);

CREATE TABLE "Set" (
	id INTEGER NOT NULL,
	co_size INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Set_id" ON "Set" (id);

CREATE TABLE "Bag" (
	id INTEGER NOT NULL,
	co_size INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Bag_id" ON "Bag" (id);

CREATE TABLE "List" (
	id INTEGER NOT NULL,
	co_size INTEGER,
	"firstItem_id" INTEGER,
	"lastItem_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("firstItem_id") REFERENCES "ListItem" (id),
	FOREIGN KEY("lastItem_id") REFERENCES "ListItem" (id)
);
CREATE INDEX "ix_List_id" ON "List" (id);

CREATE TABLE "CoElement" (
	iri TEXT NOT NULL,
	PRIMARY KEY (iri)
);
CREATE INDEX "ix_CoElement_iri" ON "CoElement" (iri);

CREATE TABLE "ListItem" (
	id INTEGER NOT NULL,
	co_index INTEGER NOT NULL,
	"itemContent" TEXT NOT NULL,
	"List_id" INTEGER,
	"ListItem_id" INTEGER,
	"nextItem_id" INTEGER,
	"previousItem_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("itemContent") REFERENCES "CoElement" (iri),
	FOREIGN KEY("List_id") REFERENCES "List" (id),
	FOREIGN KEY("ListItem_id") REFERENCES "ListItem" (id),
	FOREIGN KEY("nextItem_id") REFERENCES "ListItem" (id),
	FOREIGN KEY("previousItem_id") REFERENCES "ListItem" (id)
);
CREATE INDEX "ix_ListItem_id" ON "ListItem" (id);

CREATE TABLE "CoItem" (
	id INTEGER NOT NULL,
	"itemContent" TEXT NOT NULL,
	"Bag_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("itemContent") REFERENCES "CoElement" (iri),
	FOREIGN KEY("Bag_id") REFERENCES "Bag" (id)
);
CREATE INDEX "ix_CoItem_id" ON "CoItem" (id);

CREATE TABLE "Collection_element" (
	"Collection_id" INTEGER,
	element_iri TEXT,
	PRIMARY KEY ("Collection_id", element_iri),
	FOREIGN KEY("Collection_id") REFERENCES "Collection" (id),
	FOREIGN KEY(element_iri) REFERENCES "CoElement" (iri)
);
CREATE INDEX "ix_Collection_element_Collection_id" ON "Collection_element" ("Collection_id");
CREATE INDEX "ix_Collection_element_element_iri" ON "Collection_element" (element_iri);

CREATE TABLE "Set_element" (
	"Set_id" INTEGER,
	element_iri TEXT,
	PRIMARY KEY ("Set_id", element_iri),
	FOREIGN KEY("Set_id") REFERENCES "Set" (id),
	FOREIGN KEY(element_iri) REFERENCES "CoElement" (iri)
);
CREATE INDEX "ix_Set_element_element_iri" ON "Set_element" (element_iri);
CREATE INDEX "ix_Set_element_Set_id" ON "Set_element" ("Set_id");

CREATE TABLE "Bag_element" (
	"Bag_id" INTEGER,
	element_iri TEXT,
	PRIMARY KEY ("Bag_id", element_iri),
	FOREIGN KEY("Bag_id") REFERENCES "Bag" (id),
	FOREIGN KEY(element_iri) REFERENCES "CoElement" (iri)
);
CREATE INDEX "ix_Bag_element_element_iri" ON "Bag_element" (element_iri);
CREATE INDEX "ix_Bag_element_Bag_id" ON "Bag_element" ("Bag_id");

CREATE TABLE "List_element" (
	"List_id" INTEGER,
	element_iri TEXT,
	PRIMARY KEY ("List_id", element_iri),
	FOREIGN KEY("List_id") REFERENCES "List" (id),
	FOREIGN KEY(element_iri) REFERENCES "CoElement" (iri)
);
CREATE INDEX "ix_List_element_element_iri" ON "List_element" (element_iri);
CREATE INDEX "ix_List_element_List_id" ON "List_element" ("List_id");
