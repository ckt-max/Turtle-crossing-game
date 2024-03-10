from turtle import Screen
import time
import random
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Snake Game')
is_game_on = True

screen.tracer(0)

player = Player()
score = Scoreboard()
# car = Car()
car_list = []
screen.listen()

screen.onkeypress(player.up, 'Up')
screen.onkeyrelease(None, 'Up')
screen.onkeypress(player.down, 'Down')
screen.onkeyrelease(None, 'Down')


# initial cars
for i in range(5):
    new_car = Car()
    new_car.goto(random.randrange(-350, 350, 50), random.randrange(-200, 250, 30))
    car_list.append(new_car)

start_time = time.time()
interval = 3

while is_game_on:
    screen.update()

    current_time = time.time()
    elapsed_time = current_time - start_time

    # Generating new cars:
    if elapsed_time > interval:
        new_car = Car()
        car_list.append(new_car)
        start_time = time.time()

    for car in car_list:
        car.move(score.level)

        # Detecting player collision with the car
        if (player.ycor() < car.ycor() + 25 and player.ycor() > car.ycor() - 25) and (car.xcor() >= -50 and car.xcor() < 50):
            is_game_on = False
            score.over()
            break

        # removing cars that have crossed the road and updating the score
        if car.xcor() < -380:
            car.hideturtle()
            car_list.remove(car)
            # score.update()

    if player.ycor() > 280:
        score.score += score.level * 50
        score.level += 1
        score.update()
        player.restart()
        interval = 3/score.level



screen.exitonclick()
