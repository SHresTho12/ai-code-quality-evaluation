
def fib(n: int) -> int:
  """
  Calculates the nth Fibonacci number.

  Args:
      n: The index of the Fibonacci number to calculate (int).

  Returns:
      The nth Fibonacci number (int).
  """

  if n < 2:
    return n
  else:
    return fib(n-1) + fib(n-2)

# Example usage
print(fib(5))  # Output: 5
print(fib(8))  # Output: 21
print(fib(10))  # Output: 55
