# This is a generated Python file.
def even_odd_palindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]:
        if len(n_str) % 2 == 0:
            return "Even palindrome"
        else:
            return "Odd palindrome"
    else:
        return "Neither"
    
    
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
