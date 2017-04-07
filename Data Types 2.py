#Data Types 2
#Triple quoted strings can even span multiple lines.

message = """This message will
span several
lines."""
print message

print """This message will span
several lines
of the text."""

#Python doesn't care whether you use single  or double quotes or the three-of-a-kind quotes to surround your strings. Once it has parsed the text of your program or command, the way it stores the value is identical in all cases, and the surrounding quotes are not part of the value.

print 'This is a string.'
print """And so is this."""

#So the Python language designers usually chose to surround their strings by single quotes. What do think would happen if the string already contained single quotes?

#When you type a large integer, you might be tempted to use commas between groups of three digits, as in 42,000. This is not a legal integer in Python, but it does mean something else, which is legal.

print 42500
print 42,500

#Well, that's not what we expected at all! Because of the comma, Python chose to treat this as a pair of values. In fact, a print statement can print any numberof values as long as you separate them by commas. Notice that the values are separated by spaces when they are displayed.

print 42, 17, 56, 34, 11, 4.35, 32
print 3.4, "hello", 45

#Remember not to put commas or spaces in you integers, no matter how big they are. Make sure that you know formal languages are strict, the notation is concise, and event the smallest change might mean something quite different from what you intended.
