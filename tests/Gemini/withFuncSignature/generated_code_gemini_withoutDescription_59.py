
def largest_prime_factor(n: int) -> int:
  """
  Finds the largest prime factor of a given number.

  Args:
      n: The number to find the largest prime factor of (int).

  Returns:
      The largest prime factor of the number (int).
  """

  largest_factor = 1
  i = 2

  while i * i <= n:
    while n % i == 0:
      largest_factor = i
      n //= i
    i += 1

  if n > 1:
    largest_factor = n

  return largest_factor

# Example usage
print(largest_prime_factor(10))  # Output: 5
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(600851475143))  # Output: 6857


METADATA = {}

def check(largest_prime_factor):
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(63) == 7
    assert largest_prime_factor(330) == 11
    assert largest_prime_factor(13195) == 29

check(largest_prime_factor)