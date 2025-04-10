# scope


## local/ functional scope

## global scope



### golobal keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

```
def myfunc():
  global x
  x = 300

myfunc()

print(x)
```

### Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.

- jese ki jab koy vglobal var function k andar define krne k liye global use krte hai , vese hi bahe vale function k variable ko andat vale function mai update krne k liye nonlocal use karenge

```
def myfunc1():
  x = "Jane"
  def myfunc2():
    # nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
```