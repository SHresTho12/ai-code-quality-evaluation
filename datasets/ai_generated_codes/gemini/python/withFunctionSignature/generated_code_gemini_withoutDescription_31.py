
def is_prime(n):
  """
  Checks if a number is prime.

  Args:
      n: An integer.

  Returns:
      True if n is prime, False otherwise.

  Notes:
      - A prime number has exactly two distinct positive divisors: 1 and itself.
      - The function uses a loop to check for potential divisors from 2 to the square root of n.

  """

  if n <= 1:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True
