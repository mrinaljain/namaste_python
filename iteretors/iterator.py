
# 1. All these objects have a iter() method which is used to get an iterator:


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# Strings are also iterables 

mystr = "banana"

myStrIt = iter(mystr)

print(next(myStrIt))
print(next(myStrIt))
print(next(myStrIt))
print(next(myStrIt))
print(next(myStrIt))
print(next(myStrIt))


# 3. creating our own iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
# To prevent the iteration from going on forever, we can use the StopIteration statement.



myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# StopIteration