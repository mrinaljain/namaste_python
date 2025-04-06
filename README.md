# Python

- Python is an object oriented programming language.
- indentation is very important
- interpreted language
- Python has no command for declaring a VARIABLE.
   - A variable is created the moment you first assign a value to it.
   - Python allows you to assign values to multiple variables in one line
   ```
   x, y, z = "Orange", "Banana", "Cherry"

   ```
   - And you can assign the same value to multiple variables in one line:
   ```
   x = y = z = "Orange"

   ```

   - Unpack a Collection (destructuring as they say in Javascript)
   ```
      fruits = ["apple", "banana", "cherry"]

      x, y, z = furits

   ```
   - The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types
   ```
   str = 'Hello world'
   num = 223

   print(num , str);
   ```
   - GLOBAL variables
      - variable created outside function are global
      - variabls created inside  block or function are local
      - to create global variables inside functions 
      ```
      global x
      x = "fantastic"
      ```
      - Also, use the global keyword if you want to change a global variable inside a function. i.e the variable was declared in global scope but you want to update it from local scope.

- Data Types
   str , int, float, complex ,list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType
   - tupple and List are same but tupple is immutable and faster.






## Basic inbuilt methods 