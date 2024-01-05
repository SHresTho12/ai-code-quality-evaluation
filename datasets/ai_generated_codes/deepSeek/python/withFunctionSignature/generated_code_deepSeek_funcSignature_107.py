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