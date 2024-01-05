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


def check(histogram):
    # Check some simple cases
    assert histogram('a b b a') == {'a': 2, 'b': 2}, "Test 1"
    assert histogram('a b c a b') == {'a': 2, 'b': 2, 'c': 1}, "Test 2"
    assert histogram('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, "Test 3"
    assert histogram('r t g') == {'r': 1, 't': 1, 'g': 1}, "Test 4"
    assert histogram('b b b b a') == {'b': 4, 'a': 1}, "Test 5"
    
    # Check some edge cases that are easy to work out by hand.
    assert histogram('') == {}, "Test 6"
    assert histogram('a') == {'a': 1}, "Test 7"

check(histogram)