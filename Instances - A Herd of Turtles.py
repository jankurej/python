#Instances - A Herd of Turtles

#Just like we can have many different integers in a program, we can have many turtles. Each of them is an independent object and we call each one an instance of the Turtle type (class). Each instance has its own attributes and methods - so alex might draw with a thin black pen and be at some position, while tess might be going in her own direction with a fat pink pen. So here is what happens when alex completes a square and tess completes her triangle:

import turtle 
wn = turtle.Screen()    #Set up the window and its attributes
wn.bgcolor("lightgreen")


tess = turtle.Turtle()  #create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()  #create alex

tess.forward(80)        #Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)          #complete the triangle

tess.right(180)         #turn tess around
tess.forward(80)        #move her away from the origin

alex.forward(50)        #make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()

