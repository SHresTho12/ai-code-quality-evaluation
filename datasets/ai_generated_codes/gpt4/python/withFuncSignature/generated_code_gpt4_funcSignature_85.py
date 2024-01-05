def add(lst):
    # Initialize the sum to 0
    total = 0

    # Iterate through each element in the list and add it to the total
    for element in lst:
        total += element

    return total

# Example usage
print(add([1, 2, 3, 4]))  # Output: 10
