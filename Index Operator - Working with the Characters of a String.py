#Index Operator: Working with the Characters of a String.

#The indexing operator (Python uses square brackets to enclose the index) selects a single character from a string. The characters are accessed by their position or index value. For example, in the string shown below, the 14 characters are indexed left to right from position 0 to position 13.

#pic 3

#It is also the case that the positions are named from right to left using negative numbers where -1 is the rightmost index and so on. Note that the character at index 6 (-8) is the blank character.

school = "Luther College"
m = school[2]
print m

lastchar = school[-1]
print lastchar

#The expression school[2] selects the character at index 2 from school, and creates a new string containing just this one character. The variable m refers to the result.

#The letter at index zero of "Luther College" is L. So at position [2] we have the letter t.

#If you want the zero-eth letter of a string, you just put 0, or any expression with the value 0, in the brackets.

#The expression in brackets is called an index. An index specifies a member of an ordered collection. In this case the collection of characters in the string. The index indicates which character you want. It can be any integer expression so long as it evaluates to a valid index value.

#Note that indexing returns a string - Python has no special type for a single character. It is just a string of length 1.

