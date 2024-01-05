
def rounded_avg(n, m):
  """
  Calculates the rounded average of two numbers.

  Args:
    n: The first number.
    m: The second number.

  Returns:
    The rounded average of n and m.
  """

  average = (n + m) / 2  # Calculate the average
  rounded_average = round(average)  # Round the average to the nearest integer
  return rounded_average

# Example usage:
print(rounded_avg(5, 3))  # Output: 4
print(rounded_avg(10, 7))  # Output: 8
