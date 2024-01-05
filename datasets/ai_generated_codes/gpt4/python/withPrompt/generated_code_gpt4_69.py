def search(lst):
    """
    Find the greatest integer with a frequency greater than or equal to its value.

    Args:
    lst (list): A list of positive integers.

    Returns:
    int: The greatest integer that meets the criteria. If no such value exists, return -1.

    Examples:
    >>> search([4, 1, 2, 2, 3, 1])
    2
    >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    3
    >>> search([5, 5, 4, 4, 4])
    -1
    """
    max_integer = -1  # Initialize with -1
    max_frequency = 0

    # Create a dictionary to count the frequency of each integer
    frequency_count = {}
    for num in lst:
        if num in frequency_count:
            frequency_count[num] += 1
        else:
            frequency_count[num] = 1

    # Check each integer and its frequency
    for num, frequency in frequency_count.items():
        if num == frequency:
            # The frequency is greater than or equal to the value of the integer
            if num > max_integer:
                max_integer = num

    return max_integer
