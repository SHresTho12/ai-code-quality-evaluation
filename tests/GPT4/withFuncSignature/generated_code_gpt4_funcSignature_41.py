def car_race_collision(n: int):
    """
    Calculates the number of collision scenarios in a car race with n cars.
    Each car can move either forward or backward, leading to potential collisions.
    """
    # Base cases
    if n < 2:
        # With less than two cars, no collision is possible.
        return 0
    if n == 2:
        # With exactly two cars, there's only one possible collision.
        return 1

    # For n cars, each car has 2 choices (forward or backward), except for the
    # first car which has only 1 choice (forward) to avoid trivial no-collision scenario.
    # Therefore, the total number of scenarios is 2^(n-1).
    # However, this includes the no-collision scenario where all cars move forward.
    # So, we subtract 1 to exclude this scenario.
    return 2 ** (n - 1) - 1

# Example usage
print(car_race_collision(3))  # Example output: 3
METADATA = {} 
def check(car_race_collision): 
    assert car_race_collision(2) == 4 
    assert car_race_collision(3) == 9 
    assert car_race_collision(4) == 16 
    assert car_race_collision(8) == 64 
    assert car_race_collision(10) == 100 
    
check(car_race_collision)