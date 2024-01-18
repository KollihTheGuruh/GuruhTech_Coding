import turtle

def set_color(turtle, angle):
    if 0 <= angle < 90:
        turtle.color("yellow")
    elif 90 <= angle < 180:
        turtle.color("green")
    elif 180 <= angle < 270:
        turtle.color("pink")
    else:
        turtle.color("white")

def draw_branch(turtle, branch_length, angle, minimum_length=10):
    if branch_length > minimum_length:
        set_color(turtle, angle)
        turtle.forward(branch_length)
        turtle.left(20)
        draw_branch(turtle, branch_length * 0.8, angle)
        turtle.right(40)
        draw_branch(turtle, branch_length * 0.8, angle)
        turtle.left(20)
        turtle.backward(branch_length)
        turtle.color("white")

def draw_fractal_tree(turtle, start_length, angle, number_of_trees):
    for i in range(number_of_trees):
        current_angle = (360 / number_of_trees) * i
        turtle.setheading(current_angle)
        draw_branch(turtle, start_length, current_angle)

# Set up Turtle Graphics
turtle.tracer(0, 0)  # Turn off the animation
window = turtle.Screen()
window.bgcolor("black")

# Create Turtle object
fractal_turtle = turtle.Turtle()
fractal_turtle.speed(0)
fractal_turtle.color("white")

# Position the turtle in the center
fractal_turtle.penup()
fractal_turtle.goto(0,0)
fractal_turtle.pendown()

# Draw fractal tree
draw_fractal_tree(fractal_turtle, 100, 0, 36)

# Finish drawing and update the screen
turtle.update()

# Hide the turtle cursor and display the result
fractal_turtle.hideturtle()
window.mainloop()
