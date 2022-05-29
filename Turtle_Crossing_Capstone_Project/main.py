import time
from turtle import Screen, exitonclick
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#initialize a player turtle
user = Player()

#create a scoreboard
score_string = Scoreboard()
level = 1

screen.listen()
screen.onkey(user.move_forward, "w")

manager = CarManager()
car_creater_counter = 6

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    score_string.write_scoreboard(level)

    #create a new cars
    if car_creater_counter == 6:
        car_creater_counter = 0
        manager.create_car()
    
    car_creater_counter+=1

    #update car positions
    manager.update_cars()

    #check collisions
    result = manager.check_collisions(user)
    if result == True:
        game_is_on = False
        score_string.game_over()

    if user.finished():
        user.go_to_start()
        level+=1
        manager.increment_speed()

screen.exitonclick()
