from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

PADDLE_DISTANCE_FROM_EDGE = 40

# draw the screen with the broken line in the middle
screen = Screen()
screen.bgcolor("black")
# screenTk = screen.getcanvas().winfo_toplevel()
# screenTk.attributes("-fullscreen", True)
screen.setup(height=600, width=800)

screen_turtle = Turtle()
screen_turtle.pencolor("white")
screen_turtle.penup()
screen_turtle.hideturtle()

screen_turtle.goto(0, screen.window_height() // 2)
screen_turtle.setheading(270)
screen_turtle.width(5)
LINE_WIDTH = 20

screen.tracer(0)


def draw_screen(current_turtle, current_screen):
    while screen_turtle.ycor() - 40 > -current_screen.window_height()//2:
        current_turtle.penup()
        current_turtle.forward(LINE_WIDTH)
        current_turtle.pendown()
        current_turtle.forward(LINE_WIDTH)


draw_screen(screen_turtle, screen)

# create the pongs
left_paddle = Paddle(-screen.window_width()//2 + PADDLE_DISTANCE_FROM_EDGE)
right_paddle = Paddle(screen.window_width()//2 - PADDLE_DISTANCE_FROM_EDGE)

# create the ball object and move it
ball = Ball()

screen.update()

screen.listen()

# move the pongs using keys
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # handle ball's collision with top and bottom walls
    if ball.ycor() > screen.window_height()//2 - 10 or ball.ycor() < -screen.window_height()//2 + 10:
        ball.collision_with_wall()

    # track the collision of ball with pong
    if left_paddle.if_collision_with_ball(ball) or right_paddle.if_collision_with_ball(ball):
        ball.collision_with_paddle()


# create a score tracker
# end the game if ball crosses left or right boundary

screen.exitonclick()
