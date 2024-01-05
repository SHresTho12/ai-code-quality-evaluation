def select_words(s, n):
    """
    Selects the first 'n' words from a given string.

    :param s: The input string.
    :param n: The number of words to select.
    :return: A list containing the first 'n' words.
    """
    # Split the string into words using whitespace as the delimiter
    words = s.split()

    # Slice the list to select the first 'n' words
    selected_words = words[:n]

    return selected_words
