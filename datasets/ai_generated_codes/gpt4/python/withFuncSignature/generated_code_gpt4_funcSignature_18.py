def how_many_times(string: str, substring: str) -> int:
    """ Return the number of times 'substring' occurs in 'string'. """
    return string.count(substring)

# Example usage
test_string = "hello world, hello universe"
test_substring = "hello"
result = how_many_times(test_string, test_substring)

