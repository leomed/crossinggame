import time
from turtle import Screen
from car import Cars
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = Cars()
player = Player()
scoreboard = Scoreboard()



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.listen()
    screen.onkey(player.move_forward,"Up")

    screen.update()
    #Create new cars
    car.create_car()
    #Move the cars
    car.move_cars()

    #Detect finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car.next_level()
        scoreboard.increment_score()



    #Detec collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()


















screen.exitonclick()

