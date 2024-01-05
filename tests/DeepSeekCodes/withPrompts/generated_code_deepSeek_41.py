def car_race_collision(n: int):
    # Assuming that the cars are represented as tuples (position, direction)
    left_cars = [(0, True) for _ in range(n)]
    right_cars = [(0, False) for _ in range(n)]

    # Calculate the number of collisions
    collisions = sum(1 for left_car in left_cars for right_car in right_cars if left_car[0] == right_car[0])

    return collisions

METADATA = {} 
def check(car_race_collision): 
    assert car_race_collision(2) == 4 
    assert car_race_collision(3) == 9 
    assert car_race_collision(4) == 16 
    assert car_race_collision(8) == 64 
    assert car_race_collision(10) == 100 
    
check(car_race_collision)