#creating a heart shape using turtle
import turtle
win = turtle.Screen()
win.bgcolor("yellow")
#creating a heart shape
tur=turtle.Turtle()
tur.penup()
tur.goto(0,-200)
tur.pendown()
tur.hideturtle()
tur.begin_fill()
tur.fillcolor("red")
tur.left(45)
tur.forward(200)
tur.circle(100,180)
tur.right(90)
tur.circle(100,180)
tur.forward(200)
tur.end_fill()
while True:
    win.update()