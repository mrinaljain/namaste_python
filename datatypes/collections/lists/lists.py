# changable , allows repet values , ordered

# 1. creating list directly 
mylist = ["apple", "banana", "cherry"]

# 2. creating list using constructor

anotherList = list(("apple", "banana", "cherry"))# note the double round-brackets

print(mylist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# 3. Range querry

mylist[1:3]

# 4. Check if Item Exists

if  "item"  in mylist :
   print("if worked")

#5. Change a Range of Item Values

mylist[1:3] = ["new", "items"]  # more or les item can be insterted

#6 Insert Items without replace

mylist.insert(2, "watermelon")

#7 Append at end


# 8 add data from onelist to another (Just like merge in array)
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)