## formated strings
   # solution for string concatnation whan string needs to be merged with number

# Formated string
nu = 98
str5 = f"This is a formated {nu} string"

print(str5)


# furthur if we want to format the placeholder value 
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals

str6 = f"This is a super formates {nu:.2f} string"

str7 = f"{nu * 2}" # maths be kr sakte hai placeholder k andar

print(str6)