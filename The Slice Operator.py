#The Slice Operator

#A substring of a string is called a slice. Selecting a slice is similar to selecting a character:

singers = "Peter, Paul and Mary"
print singers[0:5]
print singers[7:11]
print singers[17:21]

#The slice operator [n:m] returns the part of the string from the n'th character to the m'th character, including the first but excluding the last. In other words, start with the character at index n and go up to but do not include the character at index m.

#If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string.

fruit = "banana"
print fruit[:3]
print fruit[3:]

