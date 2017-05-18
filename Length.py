#Length.

#The len function, when applied to a strin, returns the number of characters in a string.

fruit = "Banana"
print len(fruit)

#To get the last letter of a string, you might be tempted to try something like this:

fruit = "Banana"
sz = len(fruit)
last = fruit[sz]     # ERROR!
print last

#That won't work. It causes the runtime error "IndexError: string index out of range". The reason is that there is not letter at index position 6 in "Banana". Since we started counting at zero, the six indexes are numbered 0 to 5. To get the last character, we have to subtract 1 from length. Give it a try in the example above.

fruit = "Banana"
sz = len(fruit)
lastch = fruit[sz-1]
print lastch

#Typically, a Python programmer will access the last character by combining the two lines of code from abow.

lastch = fruit[len(fruit)-1]


