# You cannot access items in a set by referring to an index or a key.

# 1 but we can run a loop and print all elements


# 2 we can check if a value is present or not using in 

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

print("banana" not in thisset)


# 3 add new items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# 4 add new set to a set  : update method will accept any iterableas value list, array, range etc

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# 5 remove item 
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
## if item doesnot exist then it will throe error

# 5.1  solution is discard
thisset.discard("banana")

# Note: If the item to remove does not exist, discard() will NOT raise an error.


# 5.2 pop()  removes random item and returns that item


# 6 clear method will empty the set


#7 del method will delet entirly



