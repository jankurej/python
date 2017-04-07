#Data Types 1
#If you are not sure what class (data type) a value falls into, Python has a function called type which can tell you.

print type ("Hello, World!")
print type (17)
print "Hello, World"
print type (3.2)

#What about values like "17" and "3.2"? They look like numbers, but they are in quotation marks like strings.

print type ("17")
print type ("3.2")

#They're strings!
#Strings in Python can be enclosed in either single quotes (') or double quotes ("), or three of each ('''or """)

print type ('Type is a string.')
print type ("And so is this.")
print type ("""and this.""")
print type ('''and even this...''')

#Double quoted strings can contain single quotes inside them, as in "Bruce's beard", and single quoted strings can have double quotes inside them, as in 'The knights who say "Ni!"'. Strings enclosed with three occurrences of either quote symbol are called triple quoted strings. They can contain either single or double quotes.

print ('''"Oh no"''', she exclaimed, "Ben's bike is broken!"''')
