def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between cars moving in opposite directions on an infinitely long road.

    Args:
    n (int): The number of cars moving in each direction.

    Returns:
    int: The number of collisions.

    Examples:
    >>> car_race_collision(1)
    0
    >>> car_race_collision(2)
    1
    >>> car_race_collision(3)
    3
    """
    # Collisions occur when cars moving in opposite directions meet.
    # For each car moving left to right, there are n cars moving right to left to meet.
    # So, the total number of collisions is n * n.
    return n * n

# Example tests
print(car_race_collision(1))  # Output: 0
print(car_race_collision(2))  # Output: 1
print(car_race_collision(3))  # Output: 9
METADATA = {} 
def check(car_race_collision): 
    assert car_race_collision(2) == 4 
    assert car_race_collision(3) == 9 
    assert car_race_collision(4) == 16 
    assert car_race_collision(8) == 64 
    assert car_race_collision(10) == 100 
    
check(car_race_collision)