def is_palindrome(s):
    """
    Helper function to check if a string is a palindrome.

    :param s: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]

def even_odd_palindrome(n):
    """
    Checks if a given integer is a palindrome when considered as an even-length or odd-length palindrome.

    :param n: The integer to check.
    :return: True if it's a palindrome in either case, False otherwise.
    """
    str_n = str(n)
    len_n = len(str_n)
    
    # Check for even-length palindrome
    if len_n % 2 == 0:
        first_half = str_n[:len_n // 2]
        second_half = str_n[len_n // 2:]
        return is_palindrome(first_half + second_half)
    
    # Check for odd-length palindrome
    else:
        first_half = str_n[:len_n // 2]
        second_half = str_n[len_n // 2 + 1:]
        return is_palindrome(first_half + second_half)
