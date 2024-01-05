
def derivative(xs: list) -> list:
  """
  Calculates the derivative of a list of numbers representing a function.

  Args:
      xs: A list of numbers representing the function's values at different points (list).

  Returns:
      A new list containing the derivative of the function at each point (list).
  """

  if len(xs) <= 1:
    return []  # Not enough points to calculate derivative

  derivatives = []
  for i in range(1, len(xs)):
    # Calculate the slope between current and previous point
    slope = (xs[i] - xs[i-1]) / (xs[i] - xs[i-1])
    derivatives.append(slope)

  return derivatives

# Example usage
function_values = [1, 4, 9, 16, 25]
derivatives = derivative(function_values)
print(f"Function values: {function_values}")
print(f"Derivatives: {derivatives}")
