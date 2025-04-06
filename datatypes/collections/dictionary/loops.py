thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# 1 on dictionary 
for x in thisdict:
  print(x)

# 2 on the keys, values , entries 

for x in thisdict.values():
  print(x)

for  y in thisdict.keys():
  print( y)

for x, y in thisdict.items():
  print(x, y)