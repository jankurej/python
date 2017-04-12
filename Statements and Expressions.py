#A statement is an instruction that the Python interpreter can  execute. We have only seen the assignement statement and the print statement so far. Some other kinds of statements that we'll see shortly are while statements, for statements, if statements, and import statements. (There are other kinds too!)

#An expression is a combination of literals, variable names, operators, and calls to functions. Expressions need to be evaluated. The result of evaluating and expression is value or object.

#If you ask Python to print an expression, the interpreter evaluates the expression and displays the result.

print 1 + 1 + (2 *3)
print len("hello")

#In this example len is built-in Python function that returns the number of characters in a string.

#The evaluation of an expression produces a value, which is why expressions can appear on the right hand side of assignment statements. A literal all by itself is a simple expression, and so is a variable. Evaluatin a variable gives the value that the variable refers to.

y = 3.14
x = len("hello")
print x
print y

#In program, anywhere that a literal value (a string or a number) is acceptable, or more complicated expression is also acceptable. Here are all the kinds of expressions we've seen so far:
#literal - e.g. "Hello" or 3.14
#variable name - e.g. x or len
#operator expression - <expression> operator-name <expression>
#function call expression - <expression>(<expressions separated by commas>)

#Notice that operator expressions (like + and *) have sub-expressions before and after the operator. Each of these can themselves be simple or complex expressions. In that way, you can build up to having pretty complicated expressions.

print 2 * len("hello") + len("goodbye")

#Similar, when calling a function, instead of putting a literal inside the parentheses, a comples expression can be placed inside the parentheses. (Again, we provide some hidden code that defines the functions square and sub).

x = 2
y = 1
print square(y + 3)
print square(y + square(x))
print sub(square(y), square(x))

#With a function call, it;s eve possible to have a complex expression before the left parenthesis, as long as that expression evaluates to a function object. For now, though, we will just use variable names (like square, sub and len) that are directly bound to function objects.

#It is important to start learning to read code that contains complex expressions, The Python interpreter examines any line of code and parses it into components. For example, if it sees an = symbol, it will try to treat the whole line as an assignement statement. It will expect to see a valid variable name to the left of the =, and will parse everything to the right of the = as an expression. It will try to figure out whether the right side is a literal, a variable name, an operator expression or a function call expression. If its an operator expression, it will further try to parse the sub-expressions before and after the operator. And so on. You should learn to parse lines of code in the same way.

#In order to evaluate an operator expression, the Python interpreter first completely evaluates the expression before the operator, then the one after. In order to evaluate a function call expression, the inerpreter evaluates the expression before parentheses (i.e., it looks up the name of the function). Then it tries to evaluate each of the expressions inside the parentheses. There may be more than one, separated by commas. The values of those expressions are passed as inputs to the function when the function is called.

#In a funtion call expression is a sub-expression of some more complicated expression, as square(x) is in sub(square(y), square(x)), then the return value from square(x) is passed as an input to the sub function. This is one of the tricky things that you will have to get used to working out when you read (or write) code. In this example, the square function is called (twice) before the sub function is called, even though the sub function comes first when reading the code from left to right.
