# This is a generated Python file.
import random


class Car:
    def __init__(self, speed):
        self.speed = speed
        self.position = 0

    def move(self):
        self.position += self.speed

    def check_collision(self, other_car):
        return abs(self.position - other_car.position) < 1

def car_race_collision(n: int):
    cars = [Car(random.randint(1, 10)) for _ in range(n)]
    time = 0
    while True:
        for i in range(n):
            for j in range(i+1, n):
                if cars[i].check_collision(cars[j]):
                    return time
            cars[i].move()
        time += 1



METADATA = {} 
def check(car_race_collision): 
    assert car_race_collision(2) == 4 
    assert car_race_collision(3) == 9 
    assert car_race_collision(4) == 16 
    assert car_race_collision(8) == 64 
    assert car_race_collision(10) == 100 
    
check(car_race_collision)
    