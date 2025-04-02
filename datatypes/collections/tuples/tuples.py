# Tuple items are ordered, unchangeable, and allow duplicate values.



thistuple = ("apple", "banana", "cherry")
print(thistuple)


# 1. one item tuple

oneitem = ("halwa",)  # remember the comma otherwise it will be considered normal string

print(oneitem)

# 2. tuple using constructor 
# note the double round-brackets

thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)


# 3 Access Tuple Items [same as array elements]

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#3.1 Negative Indexing
# -1 refers to the last item, -2 refers to the second last item etc.


#4 Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


#5 change tuple values [workaround]
# tuple => list => change value => back to tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# 5.1 similarly we can add new values to tuple
# tuple => list => add value => back to tuple



# 5.2 another tuple can be added to a tuple easily
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

# 5.3 remove items also similar process
# tuple => list => remove value => back to tuple


# 6 unpacking tuples / Destructuring

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits;
print(green)
print(yellow)
print(red)

 #6.1 [rest operator] Assign the rest of the values as a list called "red":
# \* can be added in center also

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)