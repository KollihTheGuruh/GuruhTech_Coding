from turtle import *

def draw_heart():
    color("red")
    begin_fill()
    pensize(3)
    left(50)
    forward(133)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(133)
    end_fill()

def write_love():
    penup()
    goto(-30, -100)
    colors = ["lightcoral", "coral", "darkorange", "orangered", "red"]
    for color in colors:
        pencolor(color)
        write("Love", align="center", font=("Verdana", 24, "bold"))
        goto(xcor() + 1, ycor() - 1)

def main():
    speed(3)
    draw_heart()
    write_love()
    done()

main()
