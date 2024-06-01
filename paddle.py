from turtle import Turtle


class Paddle:

    def __init__(self, x_pos):
        self.links = []
        self.x_pos = x_pos

        for index in [-2, -1, 0, 1, 2]:
            new_link = Turtle(shape="square")
            new_link.color("white")
            new_link.penup()

            new_link.goto(x_pos, index*20)
            self.links.append(new_link)

    def move(self, direction):
        if direction == "up":
            direction = 90
        else:
            direction = 270

        for link in self.links:
            link.setheading(direction)
            link.forward(20)

    def up(self):
        self.move("up")

    def down(self):
        self.move("down")

    def if_collision_with_ball(self, ball):
        for link in self.links:
            if link.distance(ball) < 10:
                return True
        return False
