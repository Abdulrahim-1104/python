import turtle
#creating turtle for background screen
win=turtle.Screen()
win.bgcolor("blue")
win.title("Turtle Learning")
#Creating turtle
tur=turtle.Turtle()
tur.speed(1)
tur.shape("turtle")
tur.color("white")
tur.hideturtle()
tur.begin_fill()
tur.forward(100)
tur.setheading(90)
tur.forward(100)
tur.setheading(180)
tur.forward(100)
tur.setheading(270)
tur.forward(100)
tur.fillcolor("red")
tur.end_fill()
while True:
    win.update()


