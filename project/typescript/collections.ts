

/**
 * A group of things that is taken as a whole.
 */
export interface Collection {
    /** How many times the collection holds a thing, counting each repeat: the number of elements of a set, or of items of a bag or a list. */
    co_size?: number,
    /** A thing the collection holds, named by its IRI. */
    element?: string[],
}


/**
 * A collection that holds each of its elements once.
 */
export interface Set extends Collection {
}


/**
 * A collection that may hold one element more than once, in no order.
 */
export interface Bag extends Collection {
    /** An item of the bag, which holds one of its elements. */
    item?: CoItem[],
}


/**
 * A collection whose items come in order, one after another.
 */
export interface List extends Bag {
    /** The first item of the list. */
    firstItem?: ListItem,
    /** The last item of the list. */
    lastItem?: ListItem,
}


/**
 * An entry of a bag, which wraps one of the bag's elements.
 */
export interface CoItem {
    /** The element that the item wraps. */
    itemContent: string,
}


/**
 * An item of a list, which has a place in the list's order.
 */
export interface ListItem extends CoItem {
    /** The place of the item in its list, counting from 1. */
    co_index: number,
    /** The item that comes straight after this one. */
    nextItem?: ListItem,
    /** The item that comes straight before this one. */
    previousItem?: ListItem,
    /** An item that comes somewhere after this one. */
    followedBy?: ListItem[],
    /** An item that comes somewhere before this one. */
    precededBy?: ListItem[],
}



