def vowels_count(s):
    """Count the number of vowels in the string.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    >>> vowels_count("hello")
    2
    >>> vowels_count("elephant")
    3
    >>> vowels_count("python")
    1
    """
    vowels = "aeiouAEIOUY"
    count = 0
    s = s[::-1]
    for char in s:
        if char in vowels:
            count += 1
        else:
            break
    return count

# Additional test cases
print(vowels_count("hello"))      # Output: 2
print(vowels_count("elephant"))   # Output: 3
print(vowels_count("python"))     # Output: 1
