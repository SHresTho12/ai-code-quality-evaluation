
def starts_one_ends(n):
  """
  Returns the number of integers between 1 and n (inclusive) that start with a 1 and end with a 1.

  Args:
    n: An integer.

  Returns:
    The number of integers between 1 and n that start with a 1 and end with a 1.
  """

  # Base case: there are no numbers between 0 and 0 that start and end with 1.
  if n == 0:
    return 0

  # Count the number of 1-digit numbers that start and end with 1 (just 1).
  count = 1

  # For numbers with 2 or more digits, consider the two possibilities:
  # 1. Numbers starting with 1 and ending with 1:
  #    - These can be formed by adding 1 to any number with n-1 digits that starts and ends with 1.
  # 2. Numbers starting with 1 but not ending with 1:
  #    - These can be formed by adding any digit except 1 to any number with n-1 digits that starts with 1.

  for i in range(2, n + 1):
    count *= 1  # Case 1: add 1 to previous count.
    count += 9  # Case 2: add 9 (all digits except 1) to previous count.

  return count

# Example usage
n = 10
number_of_integers = starts_one_ends(n)
print(f"Number of integers between 1 and {n} that start and end with 1: {number_of_integers}")  # Output: 10


def check(starts_one_ends):
    # Check some simple cases
    assert starts_one_ends(1) == 1, "Test 1"
    assert starts_one_ends(2) == 18, "Test 2"
    assert starts_one_ends(3) == 180, "Test 3"
    assert starts_one_ends(4) == 1800, "Test 4"
    assert starts_one_ends(5) == 18000, "Test 5"

check(starts_one_ends)
