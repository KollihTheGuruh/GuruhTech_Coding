import turtle

def set_flower_color(turtle, angle):
    if 0 <= angle < 90:
        turtle.color("yellow")
    elif 90 <= angle < 180:
        turtle.color("green")
    elif 180 <= angle < 270:
        turtle.color("pink")
    else:
        turtle.color("white")

def draw_branch(turtle, branch_length, level, angle):
    if level <= 0:
        set_flower_color(turtle, angle)
        turtle.dot()  # Draw a colored dot representing the flower
        turtle.color("white")  # Reset color for the branches
    else:
        turtle.forward(branch_length)
        turtle.left(45)
        draw_branch(turtle, branch_length / 2, level - 1, angle)
        turtle.right(90)
        draw_branch(turtle, branch_length / 2, level - 1, angle)
        turtle.left(45)
        turtle.backward(branch_length)

def draw_fractal_forest(turtle, branch_length, level, num_trees):
    angle_increment = 360 / num_trees
    angle = 0
    for _ in range(num_trees):
        draw_branch(turtle, branch_length, level, angle)
        turtle.left(angle_increment)
        angle += angle_increment

# Set up the screen and turtle
turtle.bgcolor("black")
turtle.color("white")

# Speed settings
drawing_speed = 10   # Fastest (0 for no animation, 1-10 for increasing speed)
update_interval = 0 # Update screen every 'n' frames (0 for no automatic update)

turtle.speed(drawing_speed)

# Turn off the animation if drawing_speed is set to 0
if drawing_speed == 0:
    turtle.tracer(0, update_interval)

# Position the turtle
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.setheading(90)  # Start facing "north"

# Draw the fractal forest
draw_fractal_forest(turtle, 80, 5, 36)

# Update the screen after drawing is done
if drawing_speed == 0:
    turtle.update()

# Keep the window open until it's clicked
turtle.done()
