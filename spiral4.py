import turtle
import math

# Function to create a branch of the fractal tree
def draw_branch(turtle, branch_length, level):
    if level <= 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(45)
        draw_branch(turtle, branch_length / 2, level - 1)
        turtle.right(90)
        draw_branch(turtle, branch_length / 2, level - 1)
        turtle.left(45)
        turtle.backward(branch_length)

# Function to create a full 360-degree fractal tree pattern
def draw_fractal_forest(turtle, branch_length, level, num_trees):
    angle = 360 / num_trees
    for _ in range(num_trees):
        draw_branch(turtle, branch_length, level)
        turtle.left(angle)

# Set up the screen and turtle
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")
turtle.color("white")

# Position the turtle
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.setheading(90)  # Start facing "north"

# Draw the fractal forest
draw_fractal_forest(turtle, 80, 5, 36)  # Draw 36 trees to make a full circle

turtle.done()
