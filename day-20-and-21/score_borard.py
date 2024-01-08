from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as high_score_file:
            self.high_score = int(high_score_file.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f'GAME OVER', align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score - {self.score} / High Score = {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as high_score_file:
                high_score_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
