import turtle

# Square

square = turtle.Turtle()
square.setpos(-150, 150)
wn = turtle.Screen()
wn.title("Turtle")

for i in range(4):
    square.forward(50)
    square.right(90)

# Star

star = turtle.Turtle()
star.setpos(150, 150)
star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

# Polygon

polygon = turtle.Turtle()
polygon.setpos(-150, -150)

num_sides = 9
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)


# Reducing square maze

pyt = turtle.Turtle()
pyt.setpos(150, -150)


def sqrfunc(size):
    for i in range(4):
        pyt.fd(size)
        pyt.left(90)
        size = size-5


sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)

# Hypnotic mandala thingy

wn.clear()

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.speed(300)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(63)

turtle.exitonclick()
