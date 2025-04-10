import json;


#1 If you have a JSON string, you can parse it by using the json.loads() method.
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



# 2. Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# 3 Format the Result

print(json.dumps(y, indent=4, separators=(". ", " = "),sort_keys=True))
