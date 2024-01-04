
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
