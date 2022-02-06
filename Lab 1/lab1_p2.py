# APS106 Lab 1 - Drawing Shapes with Turtle
# Student Name: Chiung-Ting (Bella) Huang
# PRA Section: PRA0104


################################################
# Part 2 - Draw your initials
################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()


# use alex to draw your first and last initials
# TODO: WRITE YOUR CODE HERE

# tell alex where to go to trace the initials "B.H."

# make alex trace the letter "B"
alex.setheading(270)    # make alex face south
alex.down()             # make alex put pen down
alex.forward(100)       # make alex go 100 forward
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(50)        # make alex go 50 forward
alex.circle(25, 180)    # make alex go in circle of radius of 25 for 180 degree
alex.forward(50)        # make alex go 50 forward
alex.up()               # make alex lift the pen
alex.backward(50)       # make alex go 50 backward
alex.down()             # make alex put pen down
alex.setheading(0)      # make alex face east
alex.circle(25, 180)    # make alex go in circle of radius of 25 for 180 degree
alex.forward(50)        # make alex go 50 forward

# make alex trace a dot after the letter "B"
alex.setheading(0)      # make alex face east
alex.up()               # make alex lift the pen
alex.forward(100)       # make alex go 100 forward
alex.right(90)          # make alex turn to the right for 90 degree
alex.forward(100)       # make alex go 100 forward
alex.down()             # make alex put pen down
alex.circle(1, 360)     # make alex go in circle of radius of 1 for 360 degree
alex.up()               # make alex lift the pen

# make alex trace the letter "H"
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(75)        # make alex go 75 forward
alex.down()             # make alex put pen down
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(100)       # make alex go 100 forward
alex.up()               # make alex lift the pen
alex.backward(50)       # make alex go 50 backward
alex.down()             # make alex put pen down
alex.right(90)          # make alex turn to the right for 90 degree
alex.forward(75)        # make alex go 75 forward
alex.left(90)           # make alex turn to the left for 90 degree
alex.up()               # make alex lift the pen
alex.forward(50)        # make alex go 50 forward
alex.down()             # make alex put pen down
alex.backward(100)      # make alex go 100 backward

# make alex trace a dot after the letter "H"
alex.setheading(0)      # make alex face east
alex.up()               # make alex lift the pen
alex.forward(25)        # make alex go 25 forward
alex.down()             # make alex put pen down
alex.circle(1, 360)     # make alex go in circle of radius of 1 for 360 degree

# end of code
turtle.done()