import turtle
import random
import colorsys

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")

# Create a new turtle object
my_turtle = turtle.Turtle()
my_turtle.speed(0)

# Function to generate a random color with smooth transitions
def random_color():
    hue = random.random()
    rgb_color = colorsys.hsv_to_rgb(hue, 1, 1)
    return "#{:02x}{:02x}{:02x}".format(
        int(rgb_color[0] * 255),
        int(rgb_color[1] * 255),
        int(rgb_color[2] * 255)
    )

def draw_pattern(turtle, size, sides):
    for _ in range(sides):
        color = random_color()
        turtle.color(color)
        turtle.forward(size)
        turtle.left(360 / sides)

# Move the turtle to a starting position
my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()

# Draw patterns of increasing size to create a spiral effect
for size in range(10, 200, 10):
    draw_pattern(my_turtle, size, 6)

# Hide the turtle and display the result
my_turtle.hideturtle()
turtle.done()
