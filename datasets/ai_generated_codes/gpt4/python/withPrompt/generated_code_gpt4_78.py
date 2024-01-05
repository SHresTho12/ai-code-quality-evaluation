def hex_key(num):
    """
    Count the number of hexadecimal digits in the input string that are prime numbers.

    Args:
    num (str): The hexadecimal number as a string.

    Returns:
    int: The number of prime hexadecimal digits.

    Examples:
    >>> hex_key("AB")
    1
    >>> hex_key("1077E")
    2
    >>> hex_key("ABED1A33")
    4
    >>> hex_key("123456789ABCDEF0")
    6
    >>> hex_key("2020")
    2
    """
    
    # Define a set of prime hexadecimal digits
    prime_hex_digits = set(["2", "3", "5", "7", "B", "D"])
    
    # Convert the input string to uppercase for consistency
    num = num.upper()
    
    # Count the number of prime hexadecimal digits in the input string
    count = sum(1 for digit in num if digit in prime_hex_digits)
    
    return count
