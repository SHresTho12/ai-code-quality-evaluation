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


def check(select_words):
    # Check some simple cases
    assert select_words("Mary had a little lamb", 4) == ["little"], "Test 1"
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"], "Test 2"
    assert select_words("simple white space", 2) == [], "Test 3"
    assert select_words("Hello world", 4) == ["world"], "Test 4"
    assert select_words("Uncle sam", 3) == ["Uncle"], "Test 5"

    # Check some edge cases that are easy to work out by hand.
    assert select_words("", 4) == [], "Test 6"
    assert select_words("a b c d e f", 1) == ["b", "c", "d", "f"], "Test 7"

    # Check the function
    check(select_words)