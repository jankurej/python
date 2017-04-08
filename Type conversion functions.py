#Type conversion functions.

#Sometimes it is necessary to convert values from one type to another. Python provides a few simple functions that will allow us to do that. The functions int, float and str will (attempt to) convert their arguments into types int, float and str respectively. We call these type conversion functions.

#The int function can take a floating point number or a string, and turn it into an int. For floating point numbers, it discards the decimal portion of the number -a process we call truncation towards zero on the number line.

print 3.14, int(3.14)
print 3.9999, int(3.9999)        #This doesn't round to the closest int!     
print 3.0, int(3.0)
print-3.9999,int(-3.999)        #Note that the result is closer to zero

print "2345",int("2345")        #parse a string to produce an int
print 17,int(17)                #int even works on integers
#print int("23bottles")

#The last case shows that a string has to be a syntactically legal number, otherwise you'll get one of those pesky runtime errors. Modify the example by deleting the bottles and run the program. You should see the integer 23.

print int ("23")

#The type converter float can turn an integer, a float, or a syntactically legal string into a float.

print float ("123.45")
print type(float("123.45"))

#The type converter str turns its argument into a string. Remember that when we print a string, the quotes are removed. However, if we print the type, we can see that if is definitely str.

print str(17)
print str(123.45)
print type(str(123.45))

