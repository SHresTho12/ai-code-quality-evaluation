def anti_shuffle(s):
    """
    Takes a string and returns an ordered version of it.
    Ordered version of a string has words with characters arranged in ascending order.
    """
    # Split the input string into words
    words = s.split()

    # Initialize a list to store the ordered words
    ordered_words = []

    # Iterate through the words
    for word in words:
        # Sort the characters in the word in ascending order
        ordered_word = ''.join(sorted(word))

        # Add the ordered word to the list
        ordered_words.append(ordered_word)

    # Reconstruct the ordered string with the same word order and spaces
    ordered_string = ' '.join(ordered_words)

    return ordered_string
