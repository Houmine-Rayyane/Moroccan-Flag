import turtle

WIDTH,HEIGHT = 600,400
screen=turtle.Screen()
screen.setup(WIDTH,HEIGHT)
turtle.getscreen().bgcolor("Red")

turtle.color("green")
turtle.penup()

turtle.goto(-90,40)
turtle.pendown()
turtle.pensize(10)
for _ in range (5):
    turtle.forward(150)
    turtle.left(216)

turtle.done()