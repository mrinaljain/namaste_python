class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# syntax for inheritance
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Child(Person): 
  def __init__(self,fname,lname, year):
   super().__init__(fname, lname)
   self.graduationyear = year

#adding methods in class
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)






  