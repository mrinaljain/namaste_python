thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#1 length
print(len(thisdict))



#2 Accessing single items : 2 methods available
x = thisdict["model"]
x = thisdict.get("model")


# 3 get all keys in a list

x = thisdict.keys()  

#4 get all values

x = thisdict.values()


#5 get items (entries of key , value)


# 6 check if key exists 

if "model" in thisdict:
   print("")

#7 change items : update

thisdict.update({"year": 2020})

#8 add items 
thisdict.update({"new ": 2020})

#9 Remove items
#9.1 specific key : 2 ways
thisdict.pop("model")
del thisdict["model"]

#9.2 last inserted remove

thisdict.popitem()

#9.3 del entire dic

del thisdict

# 9.4 clear will clean dictionary


#10 Copying dictionaries 2 ways
mydict = thisdict.copy()

mydict = dict(thisdict)

