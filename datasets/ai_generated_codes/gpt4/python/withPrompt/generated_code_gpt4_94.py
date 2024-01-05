def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def largest_prime_digit_sum(lst):
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            num_str = str(num)
            for digit in num_str:
                prime_sum += int(digit)
    return prime_sum

# Test cases
print(largest_prime_digit_sum([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])) # Output: 10
print(largest_prime_digit_sum([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]))         # Output: 25
print(largest_prime_digit_sum([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3])) # Output: 13
print(largest_prime_digit_sum([0,724,32,71,99,32,6,0,5,91,83,0,5,6]))                # Output: 11
print(largest_prime_digit_sum([0,81,12,3,1,21]))                                   # Output: 3
print(largest_prime_digit_sum([0,8,1,2,1,7]))                                      # Output: 7
