A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

- False and 0 is considered the same value.
- True and 1 is considered the same value.
- Set items can be of any data type
- A set can contain different data types
- Once a set is created, you cannot change its items, but you can add new items.

## Join Sets
-   union , update : keeps both
   - union updates the first set , doesnot return 

- intersection() : keeps only common
   - & operator can also be used (only in sets)

-  difference (): method keeps the items from the first set that are not in the other set(s)
   - - operator
- symmetric_difference() : method keeps all items EXCEPT the duplicates.
   - ^ operator

- symmetric_difference_update() : method will also keep all but the duplicates, but it will change the original set instead of returning a new set.   


## Set Methods

add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others



