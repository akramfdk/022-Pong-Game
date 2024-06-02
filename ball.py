from turtle import Turtle

DEFAULT_DIRECTION = 45


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")

        self.set_ball_position()

    def set_ball_position(self):
        # set ball position
        self.goto(-self.getscreen().window_width() // 2 + 60, 0)
        self.seth(DEFAULT_DIRECTION)

    def move(self):
        self.forward(10)

    # handle ball collision with wall
    def collision_with_wall(self):
        self.seth(-self.heading())

    # handle ball collision with paddle
    def collision_with_paddle(self):
        self.seth(180 - self.heading())
