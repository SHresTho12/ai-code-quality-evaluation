def add(lst):
    """
    Given a non-empty list of integers lst, add the even elements that are at odd indices.
    """
    # Initialize the sum to 0
    even_sum = 0

    # Iterate through the list starting from the second element (odd index)
    for i in range(1, len(lst), 2):
        # Check if the element at the current index is even
        if lst[i] % 2 == 0:
            # If it's even, add it to the sum
            even_sum += lst[i]

    return even_sum
