#A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# lambda arguments : expression


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# 2 Currying 

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))