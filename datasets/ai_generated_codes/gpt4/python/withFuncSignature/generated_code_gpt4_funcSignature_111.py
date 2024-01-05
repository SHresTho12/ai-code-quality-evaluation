def histogram(test):
    """
    Creates a histogram of character frequencies in a string.

    :param test: The input string.
    :return: A dictionary where keys are characters and values are their frequencies.
    """
    # Initialize an empty dictionary to store the histogram
    char_histogram = {}

    # Iterate through the characters in the input string
    for char in test:
        # Check if the character is already in the histogram dictionary
        if char in char_histogram:
            # If it's already there, increment its frequency
            char_histogram[char] += 1
        else:
            # If it's not in the dictionary, add it with a frequency of 1
            char_histogram[char] = 1

    return char_histogram
