#creating a pong game using turtle
import turtle
#creating a window screen
win=turtle.Screen()
win.setup(600,600)
win.bgcolor("navy blue")
win.title("Pong Game")
win.tracer(0)
#Score Counting
score=turtle.Turtle()
score.hideturtle()
score.penup()
score.goto(0,280)
score.color("white")
#left paddle
left_paddle=turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=4,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-285,0)
#right paddle
right_paddle=turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=4,stretch_len=1)
right_paddle.penup()
right_paddle.goto(280,0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx=0.300
ball.dy=0.300
#moving paddle
def left_up():
    if(left_paddle.ycor()<250):
        left_paddle.sety(left_paddle.ycor()+20)
def left_down():
    if(left_paddle.ycor()>-250):
        left_paddle.sety(left_paddle.ycor()-20)
def right_up():
    if(right_paddle.ycor()<250):
        right_paddle.sety(right_paddle.ycor()+20)
def right_down():
    if(right_paddle.ycor()>-250):
        right_paddle.sety(right_paddle.ycor()-20)
win.listen()
win.onkey(left_up,'w')
win.onkey(left_down,'s')
win.onkey(right_up,'Up')
win.onkey(right_down,'Down')
#score
score_a=0
score_b=0
while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
    #bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
    #right wall
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx*=-1
        score_a+=1
        score.clear()
        score.write("Player A : {a:}  Player B : {b:}".format(a=score_a, b=score_b), align="center", font=('Arial',15,'normal'))
    #left wall
    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx*=-1
        score_b+=1
        score.clear()
        score.write("Player A : {a:}  Player B : {b:}".format(a=score_a,b=score_b),align="center",font=('Arial',15,'normal'))
    #ball touching paddle
    if ball.xcor()  > 260 and right_paddle.ycor()-50 < ball.ycor() < right_paddle.ycor()+50:
        ball.setx(260)
        ball.dx*=-1
    if ball.xcor() < -260 and left_paddle.ycor() -50 < ball.ycor() < left_paddle.ycor() +50:
        ball.setx(-260)
        ball.dx*=-1
    if score_a >= 5 or score_b >= 5:
        if score_a>=5:
            won='A'
        else:
            won='B'
        score.goto(0,0)
        score.write("GAME OVER",align="center",font=('Arial',20,'normal'))
        score.goto(0,-50)
        score.write("Players {} Won".format(won),align="center",font=('Arial',15,'normal'))
        ball.dx=0
        ball.dy=0
        score.goto(0,-100)
        score.write("Rerun To Start Again",align="center",font=('Arial',10,'normal'))
        


