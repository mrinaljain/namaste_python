# 1 Normal

a = 33
b = 200
if b > a:
  print("b is greater than a")


 # else if 

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") 
else:
  print("a is greater than b")


# shorthand 
a = 200
b = 33
c = 500

print("A") if a > b else print("B")


print("A") if a > b else print("=") if a == b else print("B")

if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")

if not a > b:
  print("a is NOT greater than b")


# 4 pass statement (in case you have nothing to execute inside if)

if b > a:
  pass
