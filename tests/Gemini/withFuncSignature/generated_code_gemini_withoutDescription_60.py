
def sum_to_n(n: int) -> int:
  """
  Calculates the sum of all natural numbers up to a given number.

  Args:
      n: The upper limit of the sum (int).

  Returns:
      The sum of all natural numbers up to n (int).
  """

  # Formula for sum of an arithmetic series: n(n + 1) / 2
  return n * (n + 1) // 2

# Example usage
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(100))  # Output: 5050


METADATA = {}

def check(sum_to_n):
    assert sum_to_n(1) == 1
    assert sum_to_n(6) == 21
    assert sum_to_n(11) == 66
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050

check(sum_to_n)
