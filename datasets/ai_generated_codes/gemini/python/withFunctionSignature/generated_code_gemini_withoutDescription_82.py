
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
