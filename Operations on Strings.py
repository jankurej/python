#Operations on Strings.

#In general, you cannot perform mathematical operations on strings, even if the strings look like numbers. The following are illegal (assuming that message has type string):

message - 1
"Hello" / 123
message * "Hello"
"15" + 2

#Interestingly, the + operator does work with strings, but for strings, the + operator represents concatention, not addition. Concatenation means joining the two operands by linking them end-to-end. 

#For example:

fruit = "banana"
bakeGood = " nut bread"
print fruit + bakedGood

#The output of this program is banana nut bread. The space before the word nut is part of the string and is necessary to produce the space between the concatenated strings. Take out the space and it again.

#The * operator also works on strings. It performs repetition. For example, 'Fun'*3 is 'FunFunFun'. One of the operands has to be a string and the other has to be an integer.

print "Go"*6

x = "Blue"
print x * 3

print "Go" *3 + x

print ("Go " + x " ") * 3

#This interpretation of + and * makes sense by analogy with addition and multiplication. Just as 4*3 is equivalent 4+4+4. we expect "Go"*3 to be the same as "Go"+"Go"+"Go", and it is. Note also in the last example that the order of operations of * and + is the same as it was for arithmetic. The repetition is done before the concatention. If you want to cause the concatention to be done first, you will need to use parentheses.

