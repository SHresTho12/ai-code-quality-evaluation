
def median(l: list) -> float:
  """Calculates the median of a list of numbers."""

  sorted_l = sorted(l)  # Sort the list to access middle elements
  middle_index = len(l) // 2  # Index of the middle element

  # Handle even and odd list lengths appropriately
  if len(l) % 2 == 0:
      # Even list: Median is the average of the two middle elements
      return (sorted_l[middle_index - 1] + sorted_l[middle_index]) / 2
  else:
      # Odd list: Median is the middle element
      return sorted_l[middle_index]
