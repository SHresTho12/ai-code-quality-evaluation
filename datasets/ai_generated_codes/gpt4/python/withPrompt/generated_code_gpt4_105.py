def by_length(arr):
    # Define a dictionary to map digits to their corresponding names
    digit_to_name = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    # Filter and sort the integers that are between 1 and 9 inclusive
    filtered_arr = sorted([x for x in arr if 1 <= x <= 9])

    # Reverse the resulting array
    reversed_arr = filtered_arr[::-1]

    # Replace each digit by its corresponding name
    result = [digit_to_name[digit] for digit in reversed_arr]

    return result

# Test cases
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
# Output: ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']

print(by_length([]))
# Output: []

print(by_length([1, -1, 55]))
# Output: ['One']
