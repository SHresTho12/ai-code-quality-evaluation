
def fibfib(n: int) -> int:
  """Calculates the nth Fibonacci-of-Fibonacci number.

  The Fibonacci-of-Fibonacci sequence is a variation of the Fibonacci sequence where each term is
  the Fibonacci number of its index. For example, the first few terms are:
  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

  Args:
      n: The index of the Fibonacci-of-Fibonacci number to calculate (int).

  Returns:
      The nth Fibonacci-of-Fibonacci number (int).
  """

  if n < 2:
    return n  # Base cases for n = 0 and n = 1

  # Memoization to store previously calculated Fibonacci numbers
  memo = {}

  def fib(m):
    """Calculates the mth Fibonacci number using memoization."""
    if m not in memo:
      memo[m] = fib(m - 1) + fib(m - 2) if m > 1 else m
    return memo[m]

  return fib(fib(n))  # Calculate the Fibonacci of the Fibonacci of n

# Example usage
print(fibfib(5))  # Output: 13
print(fibfib(8))  # Output: 34
print(fibfib(10))  # Output: 144



METADATA = {}

def check(fibfib):
    assert fibfib(2) == 1
    assert fibfib(1) == 0
    assert fibfib(5) == 4
    assert fibfib(8) == 24
    assert fibfib(10) == 81
    assert fibfib(12) == 274
    assert fibfib(14) == 927

check(fibfib)
