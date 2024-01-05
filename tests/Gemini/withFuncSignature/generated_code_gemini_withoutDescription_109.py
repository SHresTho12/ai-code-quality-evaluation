
def move_one_ball(arr):
  """
  This function moves one ball from the leftmost position of the array to the
  rightmost position.

  Args:
      arr: A list of integers representing the positions of the balls.

  Returns:
      A new list with the balls rearranged.
  """

  # Check if there are any balls in the array
  if not arr:
    return arr

  # Move the first ball to the end of the list
  first_ball = arr[0]
  arr = arr[1:]
  arr.append(first_ball)

  return arr


def check(move_one_ball):
    # Check some simple cases
    assert move_one_ball([3, 4, 5, 1, 2]) == True, "Test 1"
    assert move_one_ball([3, 5, 10, 1, 2]) == True, "Test 2"
    assert move_one_ball([4, 3, 1, 2]) == False, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert move_one_ball([3, 5, 4, 1, 2]) == False, "Test 4"
    assert move_one_ball([]) == True, "Test 5"

check(move_one_ball)
