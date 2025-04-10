# custom module
import myModule as meraModule
#inbuilt module
import platform as pf

meraModule.greeting("Jonathan")


print(meraModule.person1)

print(str(pf.processor()))


# 2  list all available functions inside module
x = dir(pf)
print(x)

# 3 Import specific things From Module
from myModule import person1

print (person1["age"])