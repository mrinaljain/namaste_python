# Booleans

- Almost any value is evaluated to True if it has some sort of content.

- Any string is True, except empty strings.

- Any number is True, except 0.

- Any list, tuple, set, and dictionary are True, except empty ones.

- empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

- **Exception** : One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False