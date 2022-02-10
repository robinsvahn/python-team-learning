import turtle, math

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