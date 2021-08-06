import time
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

t = Turtle()
t.hideturtle()
t.goto(0, 0)
t.color("white")

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")

# Animation Controller
screen.tracer(0)

# Create Paddles
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

# Paddle Movement
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# Create Ball
ball = Ball()

# Create Score Board
scoreboard = Scoreboard()

# Game On
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect miss right Paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_points()

    # Detect miss left Paddle
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_points()

    if scoreboard.p1_score >= 10:
        t.write("Game Over\n P1 Wins", align="center", font=("Courier", 25, "normal"))
        is_game_on = False
    elif scoreboard.p2_score >= 10:
        t.write("Game Over\n P2 Wins", align="center", font=("Courier", 25, "normal"))
        is_game_on = False
screen.exitonclick()
