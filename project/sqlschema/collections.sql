

CREATE TABLE "Bag" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "CoItem" (
	"itemOf" TEXT, 
	PRIMARY KEY ("itemOf")
);

CREATE TABLE "Collection" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "List" (
	element TEXT, 
	size INTEGER, 
	item TEXT, 
	"lastItem" TEXT, 
	"firstItem" TEXT, 
	PRIMARY KEY (element, size, item, "lastItem", "firstItem")
);

CREATE TABLE "ListItem" (
	"itemOf" TEXT, 
	_index INTEGER NOT NULL, 
	PRIMARY KEY ("itemOf", _index)
);

CREATE TABLE "Set" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);
