/**
 * Collection that can have a number of copies of each object
 */
export interface Bag  extends Collection  {
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * A group of objects that can be considered as a whole.
 */
export interface Collection  extends Thing  {
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * Element belonging to a bag
 */
export interface CoItem  extends Thing  {
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
}
/**
 * An ordered array of items, that can be present in multiple copies
 */
export interface List  extends Bag  {
    /**
     * The link to every item of the bag
     */item?: ListItem[],
    /**
     * The link to the last item of the list.
     */lastItem?: ListItem,
    /**
     * The link to the first item of the list.
     */firstItem?: ListItem,
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * element belonging to a list
 */
export interface ListItem  extends CoItem  {
    /**
     * A number identifying the position, starting from 1, of a particular list item within a list.
     */_index?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
}
/**
 * A collection that cannot contain duplicate elements.
 */
export interface Set  extends Collection  {
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}

export interface Thing  {
}

