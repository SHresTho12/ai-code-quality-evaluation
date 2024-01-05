def words_string(s):
    """
    Splits a string into words and returns them as a list.

    :param s: The string to be split.
    :return: A list of words in the string.
    """
    return s.split()

# Example usage
example_string = "Hello world! This is an example."
result = words_string(example_string)
result
