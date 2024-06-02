from turtle import Turtle

WINNING_SCORE = 5


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0

        self.penup()
        self.color("white")
        self.hideturtle()

        self.display_score()

    def display_score(self):
        self.clear()

        self.goto(-100, self.getscreen().window_height()//2 - 125)
        self.write(arg=self.left_score, font=("Verdana", 80, "normal"), align="center")

        self.goto(100, self.getscreen().window_height() // 2 - 125)
        self.write(arg=self.right_score, font=("Verdana", 80, "normal"), align="center")

    def increment_left_score(self):
        self.left_score += 1
        self.display_score()

    def increment_right_score(self):
        self.right_score += 1
        self.display_score()

    def check_winner(self):
        if self.left_score == WINNING_SCORE or self.right_score == WINNING_SCORE:
            self.goto(0, 0)
            if self.left_score > self.right_score:
                self.write(arg="Left Player wins !!", font=("Verdana", 30, "normal"), align="center")
            else:
                self.write(arg="Right Player wins !!", font=("Verdana", 30, "normal"), align="center")
            return True
        return False
