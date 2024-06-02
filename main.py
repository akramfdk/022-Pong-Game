from turtle import Screen, Turtle

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

PADDLE_DISTANCE_FROM_EDGE = 40
LINE_WIDTH = 20


def draw_screen():
    # draw the screen with the broken line in the middle
    current_screen = Screen()
    current_screen.bgcolor("black")
    current_screen.setup(height=600, width=800)

    current_turtle = Turtle()
    current_turtle.pencolor("white")
    current_turtle.penup()
    current_turtle.hideturtle()

    current_turtle.goto(0, current_screen.window_height() // 2)
    current_turtle.setheading(270)
    current_turtle.width(5)

    current_screen.tracer(0)

    while current_turtle.ycor() - 40 > -current_screen.window_height()//2:
        current_turtle.penup()
        current_turtle.forward(LINE_WIDTH)
        current_turtle.pendown()
        current_turtle.forward(LINE_WIDTH)

    return current_screen, current_turtle


screen, turtle = draw_screen()

# create the pongs
left_paddle = Paddle(-screen.window_width()//2 + PADDLE_DISTANCE_FROM_EDGE)
right_paddle = Paddle(screen.window_width()//2 - PADDLE_DISTANCE_FROM_EDGE)

# create the ball object and move it
ball = Ball()

# create scoreboard
scoreboard = Scoreboard()

# screen.update()
screen.listen()

# move the pongs using keys
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.03)
    ball.move()

    # handle ball's collision with top and bottom walls
    if ball.ycor() > screen.window_height()//2 - 10 or ball.ycor() < -screen.window_height()//2 + 10:
        ball.collision_with_wall()

    # track the collision of ball with pong
    if left_paddle.if_collision_with_ball(ball) or right_paddle.if_collision_with_ball(ball):
        ball.collision_with_paddle()

    # end the game if ball crosses left or right boundary
    if ball.xcor() + 10 > screen.window_width()//2:
        scoreboard.increment_left_score()
        ball.set_ball_position()
        left_paddle.reset_paddle()
        right_paddle.reset_paddle()
    elif ball.xcor() - 10 < -screen.window_width()//2:
        scoreboard.increment_right_score()
        ball.set_ball_position()
        left_paddle.reset_paddle()
        right_paddle.reset_paddle()

    if scoreboard.check_winner():
        game_is_on = False

# create a score tracker


screen.exitonclick()
