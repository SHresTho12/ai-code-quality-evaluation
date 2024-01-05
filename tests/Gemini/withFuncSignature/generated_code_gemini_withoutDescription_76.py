
def is_simple_power(x, n):
  """
  This function checks if a number is a simple power of another number.

  Args:
      x: The number to be checked.
      n: The potential base of the power.

  Returns:
      True if x is a simple power of n, False otherwise.
  """

  if x <= 0 or n <= 0:
    return False

  # Check if x is divisible by n
  if x % n != 0:
    return False

  # Repeatedly divide x by n until it becomes 1
  while x > 1:
    x //= n

  # If x is now 1, it was a simple power of n
  return x == 1

# Example usage
number = 16
base = 2
if is_simple_power(number, base):
  print(f"{number} is a simple power of {base}")
else:
  print(f"{number} is not a simple power of {base}")

def check(is_simple_power):
    # Check some simple cases
    assert is_simple_power(1, 4) == True, "Test 1"
    assert is_simple_power(2, 2) == True, "Test 2"
    assert is_simple_power(8, 2) == True, "Test 3"
    assert is_simple_power(3, 2) == False, "Test 4"
    assert is_simple_power(3, 1) == False, "Test 5"
    assert is_simple_power(5, 3) == False, "Test 6"
    
    # Check some additional simple cases
    assert is_simple_power(16, 2) == True, "Test 7"
    assert is_simple_power(143214, 16) == False, "Test 8"
    assert is_simple_power(4, 2) == True, "Test 9"
    assert is_simple_power(9, 3) == True, "Test 10"
    assert is_simple_power(16, 4) == True, "Test 11"
    assert is_simple_power(24, 2) == False, "Test 12"
    assert is_simple_power(128, 4) == False, "Test 13"
    assert is_simple_power(12, 6) == False, "Test 14"
    
    # Check some edge cases that are easy to work out by hand.
    assert is_simple_power(1, 1) == True, "Test 15"
    assert is_simple_power(1, 12) == True, "Test 16"

check(is_simple_power)
