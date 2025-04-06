def myFunc(fname):
   print("Hello " + fname + " ..!")


myFunc("Mrinal")


# If you try to call the function with more or less arguments, you will get an error:


# 2 Arbitrary Arguments, *args ()when we are not sure about no. of arguments

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#3 arguments as key value

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# 4 Arbitary named arguments(when no. is not fixed)

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# 5 use pass for empty statement


# 6 Positional-Only Arguments
def my_function(x, /):
  print(x)

my_function(3)

# 7 keyword only Arguments
def my_function(*, x):
  print(x)

my_function(x = 3)


# 8 compined 

def my_function(a, b, /, *, c, d):
 pass