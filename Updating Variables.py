#Updating Variables

#One of the most common forms of reassignment is an update where the new value of the variable depends on the old. For example:

x = x + 1

#This means get the current value of x, add one, and then update x with the new value. The new value of x is the old value of x plus 1. Although this assignment statement may look a bit strange, remember that executing assignment is a two-step process. First, evaluate the right-hand side expression. Second, let the variable name on the left-hand side refer to this new resulting object. The fact that x appears on both sides does not matter. The semantics ot the assignment statement makes sure that there is no confusion as to the result.

x = 6 #initialize x
print x
x=x+1 #update x
print x

#If you try to update a variable that doesn't exist, you get an error because Python evaluates the expression on the right side of the assignment operator before it assigns the resulting value to the name on the left. Before you can update a variable, you have to initialize it, usually with a simple assignment. In the above example, x was initialized to 6.

#Updating a variable by adding 1 is called an increment, subtracing 1 is called a decrement. Sometimes programmers also talk about bumping a variable, which means the same as incrementing it by 1.

