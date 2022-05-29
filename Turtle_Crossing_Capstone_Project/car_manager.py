COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager:
    car_list = []
    movement_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.resizemode("user")
        new_car.shapesize(stretch_wid=1, stretch_len=2, outline=0)
        new_car.color(random.choice(COLORS))
        new_car.pu()
        new_car.setpos(300,random.randint(-250,250))
        self.car_list.append(new_car)


    def update_cars(self):
        for car in self.car_list:
            car.setpos(car.xcor() - self.movement_distance, car.ycor())

            if car.xcor() < -340:
                self.car_list.remove(car)


    def check_collisions(self, user):
        collision = False
        for car in self.car_list:
            if (user.xcor() >= (car.xcor() - 20) and user.xcor() <= (car.xcor() + 20)) and ((car.ycor() - user.ycor()) < 20 and (car.ycor() - user.ycor()) > 0):
                collision = True
        return collision

    
    def increment_speed(self):
        self.movement_distance += MOVE_INCREMENT