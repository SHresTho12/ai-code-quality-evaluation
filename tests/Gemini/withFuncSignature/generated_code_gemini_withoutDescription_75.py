
def is_multiply_prime(a):
  """
  This function checks if a number is a product of two distinct primes.

  Args:
      a: The number to be checked.

  Returns:
      True if a is a product of two distinct primes, False otherwise.
  """

  if a <= 1:
    return False

  # Check if a is even
  if a % 2 == 0:
    return a == 4  # 4 is the only even prime number

  # Check for divisibility by 3
  if a % 3 == 0:
    return False

  # Check for divisibility by other primes up to the square root of a
  for i in range(5, int(a**0.5) + 1, 6):
    if a % i == 0 or a % (i + 2) == 0:
      return False

  # If no factors found, a is a product of two distinct primes
  return True

# Example usage
number = 12
if is_multiply_prime(number):
  print(f"{number} is a product of two distinct primes")
else:
  print(f"{number} is not a product of two distinct primes")


def check(is_multiply_prime):
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(8) == True
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(125) == True
    assert is_multiply_prime(3 * 5 * 7) == True
    assert is_multiply_prime(3 * 6 * 7) == False
    assert is_multiply_prime(9 * 9 * 9) == False
    assert is_multiply_prime(11 * 9 * 9) == False
    assert is_multiply_prime(11 * 13 * 7) == True

check(is_multiply_prime)
