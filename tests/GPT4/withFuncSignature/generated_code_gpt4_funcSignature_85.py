def add(lst):
    # Initialize the sum to 0
    total = 0

    # Iterate through each element in the list and add it to the total
    for element in lst:
        total += element

    return total

# Example usage
print(add([1, 2, 3, 4]))  # Output: 10



def check(add):
    # Check some simple cases
    assert add([4, 88]) == 88, "Test 1"
    assert add([4, 5, 6, 7, 2, 122]) == 122, "Test 2"
    assert add([4, 0, 6, 7]) == 0, "Test 3"
    assert add([4, 4, 6, 8]) == 12, "Test 4"

    # Check some edge cases that are easy to work out by hand.

check(add)