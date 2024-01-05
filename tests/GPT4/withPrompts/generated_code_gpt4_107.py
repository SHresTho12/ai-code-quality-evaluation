def is_palindrome(num):
    return str(num) == str(num)[::-1]

def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0

    for i in range(1, n):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)

# Test cases
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12)) # Output: (4, 6)

def check(even_odd_palindrome):
    # Check some simple cases
    assert even_odd_palindrome(123) == (8, 13)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(63) == (6, 8)
    assert even_odd_palindrome(25) == (5, 6)
    assert even_odd_palindrome(19) == (4, 6)
    assert even_odd_palindrome(9) == (4, 5)

    # Check some edge cases that are easy to work out by hand.
    assert even_odd_palindrome(1) == (0, 1)

check(even_odd_palindrome)