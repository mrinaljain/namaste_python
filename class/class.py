# defining class
class myClass:
   x =10


# creating instance of class
classTen = myClass();


print(classTen.x)


# __init__() function (class constructor)
# __str__() function  (toString method)
class myAnotherClass:
   def __init__(self, key1, key2):  # slef bole to this keyword 
      self.key1 = key1
      self.key2 = key2

   def __str__(self):
      return self.x
   
   x = 10

anotherClass = myAnotherClass("key1", "key2")
ans = anotherClass.__str__();

print(ans)


# Object Methods

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()