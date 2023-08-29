#creating circle using turtle
import  turtle
win = turtle.Screen()
win.bgcolor("yellow")
#creating a turtle
tur=turtle.Turtle()
tur.shape("turtle")
#creating a circle using circle method
tur.hideturtle()
tur.begin_fill()
tur.fillcolor("orange")
tur.circle(100)
tur.end_fill()
while True:
    win.update()