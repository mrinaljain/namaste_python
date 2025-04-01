
# Remove element (single Item only)
thislist = ["apple", "banana", "cherry","banana"]
thislist.remove("banana")
thislist.remove("banana")
print(thislist)

# 2. Remove specific index
#If you do not specify the index, the pop() method removes the last item.


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# 3. Delete entire list

thislist = ["apple", "banana", "cherry"]
del thislist



#4 Clear the list 

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# 5 Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# 6 sort method 
# sorts in lexiographic manner / also the numbers 
# sort() is case sensetive , Capital is given first pref no matter what
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# 6.1 descending sort 

thislist.sort(reverse = True)

# 6.2 sort with conparator function
def myfunc(n):
  return abs(n - 50) # smallest first

#Sort the list based on how close the number is to 50:
thislist.sort(key = myfunc)

print(thislist)


# 7 Reverse the list 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)