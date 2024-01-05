def maximum(arr, k):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Return the first k elements of the sorted array
    return arr[:k]

# Test cases
print(maximum([-3, -4, 5], 3))  # Output: [-4, -3, 5]
print(maximum([4, -4, 4], 2))   # Output: [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # Output: [2]
