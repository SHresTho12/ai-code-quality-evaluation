def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in the basket.

    Args:
    s (str): A string representing the distribution of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.

    Examples:
    >>> fruit_distribution("5 apples and 6 oranges", 19)
    8
    >>> fruit_distribution("0 apples and 1 oranges", 3)
    2
    >>> fruit_distribution("2 apples and 3 oranges", 100)
    95
    >>> fruit_distribution("100 apples and 1 oranges", 120)
    19
    """
    # Split the input string by spaces
    words = s.split()

    # Initialize variables to store the counts of apples and oranges
    apples_count = 0
    oranges_count = 0

    # Iterate through the words to find counts of apples and oranges
    for i in range(len(words)):
        if words[i] == "apples":
            # Get the number of apples as the previous word (converted to int)
            apples_count = int(words[i - 1])
        elif words[i] == "oranges":
            # Get the number of oranges as the previous word (converted to int)
            oranges_count = int(words[i - 1])

    # Calculate the number of mangoes as the difference between total fruits and apples and oranges
    mango_count = n - apples_count - oranges_count

    return mango_count
