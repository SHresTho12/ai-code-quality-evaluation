
def prime_fib(n: int):
  """
  Generates the first n Fibonacci numbers where all prime numbers are removed.

  Args:
      n: The number of Fibonacci numbers to generate.

  Yields:
      The next Fibonacci number that is not a prime number.
  """

  # Initialize the first two Fibonacci numbers.
  a, b = 0, 1

  # Keep track of the number of Fibonacci numbers generated.
  count = 0

  # Use a set to store encountered prime numbers for faster lookup.
  primes = set()

  while count < n:
    # Check if the current Fibonacci number is prime.
    if is_prime(b):
      primes.add(b)
    else:
      # Yield the current Fibonacci number if it's not prime.
      yield b
      count += 1

    # Calculate the next Fibonacci number.
    a, b = b, a + b

def is_prime(n: int):
  """
  Checks if a number is prime.

  Args:
      n: The number to check.

  Returns:
      True if the number is prime, False otherwise.
  """

  if n <= 1:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True

# Example usage
for i in prime_fib(10):
  print(i)


METADATA = {} 
def check(prime_fib): 
    assert prime_fib(1) == 2 
    assert prime_fib(2) == 3 
    assert prime_fib(3) == 5 
    assert prime_fib(4) == 13 
    assert prime_fib(5) == 89 
    assert prime_fib(6) == 233 
    assert prime_fib(7) == 1597 
    assert prime_fib(8) == 28657 
    assert prime_fib(9) == 514229 
    assert prime_fib(10) == 433494437 

check(prime_fib)