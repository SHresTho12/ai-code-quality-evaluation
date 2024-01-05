
def largest_divisor(n: int) -> int:
  """
  Finds the largest divisor of a positive integer n, excluding 1 and n itself.

  Args:
      n: A positive integer.

  Returns:
      An integer representing the largest divisor of n, or 1 if n is 1 or a prime number.

  Notes:
      - The function uses a loop to iterate through potential divisors from n-1 down to 2.
      - If a divisor divides n evenly, it is returned.

  """

  if n <= 1:
    return 1

  # Start with the largest potential divisor (n-1) and work down.
  for i in range(n - 1, 1, -1):
    if n % i == 0:
      return i

  # If no divisor is found, n is a prime number.
  return 1

# Example usage
test_numbers = [12, 25, 31, 40]
for num in test_numbers:
  largest_div = largest_divisor(num)
  print(f"Largest divisor of {num}: {largest_div}")


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(largest_divisor): 
    assert largest_divisor(3) == 1 
    assert largest_divisor(7) == 1 
    assert largest_divisor(10) == 5 
    assert largest_divisor(100) == 50 
    assert largest_divisor(49) == 7 
    
check(largest_divisor)