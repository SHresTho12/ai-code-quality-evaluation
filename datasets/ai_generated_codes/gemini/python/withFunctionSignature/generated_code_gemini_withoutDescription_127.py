
def intersection(interval1, interval2):
  """
  Finds the intersection of two intervals represented by tuples.

  Args:
      interval1: A tuple of two numbers representing the first interval (start, end).
      interval2: A tuple of two numbers representing the second interval (start, end).

  Returns:
      A tuple representing the intersection interval, or None if there is no intersection.
  """
  start1, end1 = interval1
  start2, end2 = interval2

  # Check if the intervals overlap at all
  if end1 < start2 or end2 < start1:
    return None

  # Find the starting point of the intersection
  intersection_start = max(start1, start2)

  # Find the ending point of the intersection
  intersection_end = min(end1, end2)

  # Return the intersection interval as a tuple
  return (intersection_start, intersection_end)

# Example usage
interval1 = (1, 5)
interval2 = (3, 7)
intersection = intersection(interval1, interval2)

if intersection:
  print(f"Intersection of {interval1} and {interval2} is {intersection}")
else:
  print(f"{interval1} and {interval2} do not intersect")
