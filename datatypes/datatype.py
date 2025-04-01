a = str("Hello");
print("String Data type =>", a)


c = float(6)
print("float Data type =>", c)

d = 5j
d1 = 3 +6j
print("Complex Data type =>", d)

# n Python, the complex data type is used to represent complex numbers, which have a real and an imaginary part. The imaginary part is denoted with a j


e = [2,3,4,5]
print("List Data type =>", e)


f = ("apple", "banana", "cherry")
print("Tupple Data type =>", f)


g = range(6)
g1 = range(2 , 20, 2)  # range(start, stop[, step]) -> range object
print("Range Data type =>", g)
print("Range Data type =>", g1)


h = {"name": "Mrinal", "isGood" : True} # map or dictionary types
print("Dict Data type =>",h)

i =  {1,2,3,4,5,4,3,2,1}  # unique values
print("SET Data type =>",i);

j = frozenset({"apple", "banana", "cherry"}) # Can not be updated
print("Frozen SET Data type =>",j);

