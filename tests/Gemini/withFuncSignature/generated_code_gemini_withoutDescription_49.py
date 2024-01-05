
def modp(n: int, p: int) -> int:
  """
  Calculates the modulo of a number n with respect to a modulus p.

  Args:
      n: The number to calculate the modulo for (int).
      p: The modulus (int).

  Returns:
      The remainder of dividing n by p (int).
  """

  # Handle negative numbers
  if n < 0:
    n = abs(n)

  # Calculate the modulo using the remainder operator
  return n % p

# Example usage
print(modp(10, 3))  # Output: 1
print(modp(-12, 5))  # Output: 2
print(modp(255, 16))  # Output: 15



METADATA = {}

def check(modp):
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
    assert modp(30, 5) == 4
    assert modp(31, 5) == 3

check(modp)
