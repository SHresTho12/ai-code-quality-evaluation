def get_positive(l: list) -> list:
    """ Return a list containing only the positive numbers from the input list. """
    return [num for num in l if num > 0]

# Example usage
test_list = [1, -2, 3, -4, 5, -6]
result = get_positive(test_list)
result
