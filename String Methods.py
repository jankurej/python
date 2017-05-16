#String Methods.

#The "dot notation" is the way we connect an object to one of its attributes or to invoke a method on that object. There are a wide variety of methods for string objects. Try the following program:

ss = "Hello, World"
print ss.upper()


tt = ss.lower()
print tt

#In this example, upper is a method that can be invoked on any string object to create a new string in which all the characters are in uppercase. lowe works in a similar fashion changing all characters in the string to lowercase. (The original string ss remains unchanged. A new string tt is created.)

#In addition to upper and lower, the following table provides a summary of some other useful string methods. There are a few activecode exampple that follow so that you can try them out. (upper, lower, capitalize, strip, lstrip, rstrip, count, replace, center, ljust, rjust, find, rfind, index, rindex)

#We can experiment with these methods so that we understand what they do. Note once again that the methods that return strings do not change the original.

#Code 1

ss = "   Hello, World   "

els = ss.count("1")
print els

print "***"+ss.strip()+"***"
print "***"+ss.lstrip()+"***"
print "***"+ss.rstrip()+"***"

news = ss.replace("o","***")
print news

#Code 2

food = "banana bread"
print food.capitalize()

print "*"+food.center(25)+"*"
print "*"+food.ljust(25)+"*"      #stars added to show bounds
print "*" +food.rjust(25)+"*"

print food.find("e")
print food.find("na")
print food.find("b")

print food.rfind("e")
print food.rfind("na")
print food.rfind("b")

print food.index("e")


