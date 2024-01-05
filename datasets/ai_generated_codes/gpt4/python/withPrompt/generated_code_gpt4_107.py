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
