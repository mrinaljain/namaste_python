# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.



import datetime as date



time = date.datetime.now()


print(time)


# 2 Creating Date Objects

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)


# 3 Date time formating methods

# 3.1 The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))