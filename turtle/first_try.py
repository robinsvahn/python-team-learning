import turtle
# skk = turtle.Turtle()

# for i in range(4):
#     skk.forward(50)
#     skk.right(90)

# ###########################################

# star = turtle.Turtle()
# star.right(75)
# star.forward(100)

# for i in range(4):
#     star.right(144)
#     star.forward(100)

# ###########################################

# polygon = turtle.Turtle()

# num_sides = 9
# side_length = 70
# angle = 360.0 / num_sides

# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)


# ##########################################

# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# pyt = turtle.Turtle()
# pyt.color("blue")


# def sqrfunc(size):
#     for i in range(4):
#         pyt.fd(size)
#         pyt.left(90)
#         size = size-5


# sqrfunc(146)
# sqrfunc(126)
# sqrfunc(106)
# sqrfunc(86)
# sqrfunc(66)
# sqrfunc(46)
# sqrfunc(26)

# ##########################################

# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# t.speed(100)
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x % 6])
#     t.width(x//100 + 1)
#     t.forward(x)
#     t.left(69)

import math

olympic_pen = turtle.Pen()
colors = ["blue", "black", "red", "orange", "green"]

olympic_pen.color("red")
olympic_pen.width(5)
olympic_pen.speed(50)
olympic_pen.penup()
olympic_pen.setpos(-220, 25)
olympic_pen.pendown()

halfpoint = math.ceil(len(colors) / 2)

for color in colors:
    if(halfpoint == 0):
        olympic_pen.penup()
        olympic_pen.setpos(-110, -80)
        olympic_pen.pendown()
    olympic_pen.color(color)
    olympic_pen.circle(100)
    olympic_pen.penup()
    olympic_pen.forward(220)
    olympic_pen.pendown()

    halfpoint -= 1


turtle.exitonclick()
