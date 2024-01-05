
def fib4(n: int) -> int:
  """
  Calculates the nth Fib4 number, a variation of the Fibonacci sequence defined as:
  fib4(0) = 0
  fib4(1) = 0
  fib4(2) = 2
  fib4(3) = 0
  fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n > 3

  Args:
      n: The index of the Fib4 number to calculate (int).

  Returns:
      The nth Fib4 number (int).
  """

  results = [0, 0, 2, 0]  # Initialize the first four Fib4 numbers

  if n < 4:
    return results[n]  # Base cases for n = 0, 1, 2, 3

  # Iteratively calculate the remaining Fib4 numbers
  for i in range(4, n + 1):
    results.append(results[-1] + results[-2] + results[-3] + results[-4])

  return results[n]  # Return the nth Fib4 number

# Example usage:
print(fib4(5))  # Output: 4
print(fib4(8))  # Output: 28
print(fib4(10))  # Output: 104

METADATA = {} 
def check(fib4): 
    assert fib4(5) == 4 
    assert fib4(8) == 28 
    assert fib4(10) == 104 
    assert fib4(12) == 386 
    
check(fib4)
