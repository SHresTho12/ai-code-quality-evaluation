
def rounded_avg(n, m):
  """
  Calculates the rounded average of two numbers.

  Args:
    n: The first number.
    m: The second number.

  Returns:
    The rounded average of n and m.
  """

  average = (n + m) / 2  # Calculate the average
  rounded_average = round(average)  # Round the average to the nearest integer
  return rounded_average

# Example usage:
print(rounded_avg(5, 3))  # Output: 4
print(rounded_avg(10, 7))  # Output: 8


def check(rounded_avg):
    assert rounded_avg(1, 5) == "0b11", "Test 1"
    assert rounded_avg(7, 13) == "0b1010", "Test 2"
    assert rounded_avg(964, 977) == "0b1111001010", "Test 3"
    assert rounded_avg(996, 997) == "0b1111100100", "Test 4"
    assert rounded_avg(560, 851) == "0b1011000010", "Test 5"
    assert rounded_avg(185, 546) == "0b101101110", "Test 6"
    assert rounded_avg(362, 496) == "0b110101101", "Test 7"
    assert rounded_avg(350, 902) == "0b1001110010", "Test 8"
    assert rounded_avg(197, 233) == "0b11010111", "Test 9"

# Check some edge cases that are easy to work out by hand.
assert rounded_avg(7, 5) == -1, "Edge Test 1"
assert rounded_avg(5, 1) == -1, "Edge Test 2"
assert rounded_avg(5, 5) == "0b101", "Edge Test 3"

check(rounded_avg)
