import turtle
import random

# Function to draw a single square with enhanced graphics and different colors
def enhanced_square(t, length):
    for _ in range(4):
        t.color(random.random(), random.random(), random.random())  # Random RGB color
        t.forward(length)
        t.right(90)

# Function to draw the complete pattern with enhanced graphics and different colors
def draw_enhanced_pattern(t, squares, step):
    for _ in range(squares):
        enhanced_square(t, step)
        t.forward(step)
        t.right(90)
        step += 10

# Create a turtle object with enhanced attributes
my_turtle = turtle.Turtle()
my_turtle.speed(2)  # Set drawing speed to a moderate value
my_turtle.pensize(2)  # Set pen size to 2 for a bolder appearance

# Draw the enhanced pattern with 50 squares and initial step of 10
draw_enhanced_pattern(my_turtle, 50, 10)

# Hide the turtle and display the drawing
my_turtle.hideturtle()
turtle.done()
