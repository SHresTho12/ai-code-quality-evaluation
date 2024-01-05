
def prime_length(string):
  """
  Returns the length of the longest substring of the given string that consists
  only of prime numbers (as characters).

  Args:
    string: A string containing characters representing numbers.

  Returns:
    The length of the longest substring of prime numbers.
  """

  # Create a dictionary to store whether a number is prime.
  is_prime = {2: True}
  for num in range(3, 100):
    is_prime[num] = all(num % i != 0 for i in range(2, int(num**0.5) + 1))

  # Keep track of the current substring length and the maximum length.
  current_length, max_length = 0, 0
  for char in string:
    if is_prime.get(int(char)):
      current_length += 1
    else:
      max_length = max(max_length, current_length)
      current_length = 0

  # Update the maximum length with the last substring.
  max_length = max(max_length, current_length)
  return max_length

# Example usage
string = "3125710"
longest_prime_substring = prime_length(string)
print(f"Longest substring of prime numbers: {longest_prime_substring}")  # Output: 3


def check(prime_length):
    # Check some simple cases
    assert prime_length('Hello') == True, "Test 1"
    assert prime_length('abcdcba') == True, "Test 2"
    assert prime_length('kittens') == True, "Test 3"
    assert prime_length('orange') == False, "Test 4"
    assert prime_length('wow') == True, "Test 5"
    assert prime_length('world') == True, "Test 6"
    assert prime_length('MadaM') == True, "Test 7"
    assert prime_length('Wow') == True, "Test 8"
    assert prime_length('') == False, "Test 9"
    assert prime_length('HI') == True, "Test 10"
    assert prime_length('go') == True, "Test 11"
    assert prime_length('gogo') == False, "Test 12"
    assert prime_length('aaaaaaaaaaaaaaa') == False, "Test 13"

check(prime_length)
