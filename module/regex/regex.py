import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


# findall :	Returns a list containing all matches
#search: 	Returns a Match object if there is a match anywhere in the string
# split:	Returns a list where the string has been split at each match
# sub	: Replaces one or many matches with a string