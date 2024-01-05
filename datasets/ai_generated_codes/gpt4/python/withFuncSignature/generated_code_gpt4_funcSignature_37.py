def sort_even(l: list):
    # Filter out even numbers and sort them
    return sorted([x for x in l if x % 2 == 0])

# Example usage
print(sort_even([5, 3, 2, 8, 1, 4]))  # Output: [2, 4, 8]
