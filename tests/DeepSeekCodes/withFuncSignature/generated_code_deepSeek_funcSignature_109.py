# This is a generated Python file.
def move_one_ball(arr):
    return sorted(arr, key=lambda x: x==1)


def check(move_one_ball):
    # Check some simple cases
    assert move_one_ball([3, 4, 5, 1, 2]) == True, "Test 1"
    assert move_one_ball([3, 5, 10, 1, 2]) == True, "Test 2"
    assert move_one_ball([4, 3, 1, 2]) == False, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert move_one_ball([3, 5, 4, 1, 2]) == False, "Test 4"
    assert move_one_ball([]) == True, "Test 5"

check(move_one_ball)
