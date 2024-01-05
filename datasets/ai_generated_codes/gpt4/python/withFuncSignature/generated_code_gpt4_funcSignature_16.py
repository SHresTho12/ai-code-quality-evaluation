def count_distinct_characters(string: str) -> int:
    """ Return the number of distinct characters in the given string. """
    return len(set(string))

# Testing the function
test_string = "hello world"
result = count_distinct_characters(test_string)
result
