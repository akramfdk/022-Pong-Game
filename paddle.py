from turtle import Turtle
import turtle


class Paddle:

    def __init__(self, x_pos):
        self.links = []
        self.x_pos = x_pos

        for index in range(5):  # [-2, -1, 0, 1, 2]:
            new_link = Turtle(shape="square")
            new_link.color("white")
            new_link.penup()

            new_link.goto(x_pos, (index - 2) * 20)
            self.links.append(new_link)

    def reset_paddle(self):
        for index, link in enumerate(self.links):
            link.goto(self.x_pos, (index - 2) * 20)

    def move(self, direction):
        if direction == "up":
            gap = turtle.getscreen().window_height() // 2 - (self.links[-1].ycor() + 10)
            direction = 90
        else:
            gap = (self.links[0].ycor() - 10) + turtle.getscreen().window_height() // 2
            direction = 270

        if gap < 0:
            return

        for link in self.links:
            link.setheading(direction)
            if gap >= 20:
                link.forward(20)
            else:
                link.forward(gap)

    def up(self):
        self.move("up")

    def down(self):
        self.move("down")

    def if_collision_with_ball(self, ball):
        if ball.xcor() >= 0:
            distance_from_wall = turtle.getscreen().window_width() - ball.xcor()
        else:
            distance_from_wall = abs(-turtle.getscreen().window_width() + ball.xcor())

        for link in self.links:
            if link.distance(ball) < 10 and distance_from_wall > 50:
                return True
        return False
