from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.score = 0
        self.goto(-325, 250)
        self.write(f'Score: {self.score}', move=False, align='center', font=('Raleway', 15, 'bold'))
        self.goto(325, 250)
        self.write(f'Level {self.level}', move=False, align='center', font=('Raleway', 15, 'bold'))

    def update(self):
        self.clear()
        self.goto(-325, 250)
        self.write(f'Score: {self.score}', move=False, align='center', font=('Raleway', 15, 'bold'))
        self.goto(325, 250)
        self.write(f'Level {self.level}', move=False, align='center', font=('Raleway', 15, 'bold'))

    def over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align='center', font=('Raleway', 45, 'bold'))


