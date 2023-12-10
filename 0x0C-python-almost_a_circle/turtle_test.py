#!/usr/bin/python3
import turtle

# Create a turtle screen and a turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Draw a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

# Close the turtle graphics window on click
screen.exitonclick()
