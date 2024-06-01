from turtle import Turtle

INITIAL_BALL_DIRECTION = 45


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")

        # set initial position and direction of ball
        self.setx(-self.getscreen().window_width() // 2 + 60)
        self.seth(INITIAL_BALL_DIRECTION)

    def move(self):
        self.forward(10)

    # handle ball collision with wall
    def collision_with_wall(self):
        self.seth(-self.heading())

    # handle ball collision with paddle
    def collision_with_paddle(self):
        self.seth(180 - self.heading())
