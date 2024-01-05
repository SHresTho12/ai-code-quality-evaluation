
def get_odd_collatz(n):
  """
  Generates a list of all odd numbers in the Collatz sequence starting from n.

  Args:
      n: The starting number for the Collatz sequence.

  Returns:
      A list containing all odd numbers in the Collatz sequence starting from n.
  """
  sequence = []
  while n % 2 != 0:
    sequence.append(n)
    if n == 1:
      break
    if n % 4 == 1:
      n = 3 * n + 1
    else:
      n //= 2
  return sequence


def check(get_odd_collatz):
    # Check some simple cases
    assert get_odd_collatz(14) == [1, 5, 7, 11, 13, 17], "Test 1"
    assert get_odd_collatz(5) == [1, 5], "Test 2"
    assert get_odd_collatz(12) == [1, 3, 5], "Test 3"

    # Check the function
    check(get_odd_collatz)