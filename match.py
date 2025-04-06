
# The match statement is used to perform different actions based on different conditions. 
# just like switch statement

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5  if month == 4:   # extart condition can also be added
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Looking forward to the Weekend")