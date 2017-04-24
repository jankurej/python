#Reassignment

#As we have mentioned previously, it is legal to make more than one assignment to the same variable. A new assignment makes an existing variable refer to a new value (and stop referring to the old value).

bruce = 5
print bruce
bruce = 7
print bruce

#The first time bruce is printed, its value is 5, and the second time, its value is 7. The assignment statement changes the value (the object) that bruce refers to.

#Here is what reassignment looks like in a reference diagram:
#pic#2

#It is important to note tha in mathematics, a statement of equality is always true. If a is equal to b now, then a will always equal to b. In Python, an assignment statement can make two variables refer to the same object and therefore have the same value. They appear to be equal. However, because of the possibility of reassignment, they don't have to stay that way:

a = 5
b = a       #after executing this line, a and b are now equal
print a,b
a = 3 #after executing this line, a and b are no longer equal
print a,b

#Line 4 changes the value of a but does not change the value of b, so they are no longer equal. We will have much more to say about equality in a later chapter.

