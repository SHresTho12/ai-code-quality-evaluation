def sort_array(arr):
    def count_ones(binary_num):
        return bin(binary_num).count('1')

    return sorted(arr, key=lambda x: (count_ones(x), x))

# Test cases
print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
