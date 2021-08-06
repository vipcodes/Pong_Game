from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-80, 250)
        self.write(f"P1:{self.p1_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(80, 250)
        self.write(f"P2:{self.p2_score}", align="center", font=("Courier", 20, "normal"))

    def l_points(self):
        self.p1_score += 1
        self.update_scoreboard()

    def r_points(self):
        self.p2_score += 1
        self.update_scoreboard()
