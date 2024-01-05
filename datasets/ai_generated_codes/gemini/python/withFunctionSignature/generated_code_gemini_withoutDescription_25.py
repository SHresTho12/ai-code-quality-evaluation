
from typing import List

def factorize(n: int) -> List[int]:
  """
  Finds the prime factorization of a positive integer n.

  Args:
      n: A positive integer.

  Returns:
      A list of integers representing the prime factors of n, in ascending order.

  Notes:
      - The function uses trial division to find factors.
      - If n is prime, the list will only contain n itself.

  """

  if n <= 1:
    return []

  factors = []
  # Start with the smallest potential prime factor (2).
  divisor = 2
  while divisor * divisor <= n:
    if n % divisor == 0:
      factors.append(divisor)
      n //= divisor
    else:
      divisor += 1

  # If n is not divisible by any factor found so far, it is prime.
  if n > 1:
    factors.append(n)

  return factors

# Example usage
test_numbers = [12, 25, 31, 40]
for num in test_numbers:
  prime_factors = factorize(num)
  print(f"Prime factors of {num}: {prime_factors}")
