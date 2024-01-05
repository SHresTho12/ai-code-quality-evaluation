def move_one_ball(arr):
    # Check if the array is empty or has only one element
    if not arr or len(arr) == 1:
        return True

    # Find the minimum element in the array
    min_element = min(arr)

    # Find the index of the minimum element
    min_index = arr.index(min_element)

    # Calculate the expected sorted array
    expected_sorted = sorted(arr)

    # Check if the original array can be obtained by right-shifting
    for i in range(len(arr)):
        shifted_arr = [arr[(min_index + j) % len(arr)] for j in range(len(arr))]
        if shifted_arr == expected_sorted:
            return True

    return False

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
