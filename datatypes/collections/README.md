# Collections 


There are four collection data types in the Python programming language:

1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.


| Collection Type | Mutable (Changable) | Immutable (Unchangable) | Allows Duplicates | Ordered? |
|----------------|---------------------|-------------------------|-------------------|----------|
| **List**       | ✅ Yes               | ❌ No                   | ✅ Yes           | ✅ Yes   |
| **Tuple**      | ❌ No                | ✅ Yes                  | ✅ Yes           | ✅ Yes   |
| **Set**        | ❌ No* (Items cannot be changed, but new items can be added/removed) | ✅ Yes (Individual elements) | ❌ No | ❌ No (Unordered) |
| **Dictionary** | ✅ Yes (Keys cannot be changed, but values can) | ❌ No | ❌ No (Keys must be unique, but values can be duplicate) | ✅ Yes (Python 3.7+) |
