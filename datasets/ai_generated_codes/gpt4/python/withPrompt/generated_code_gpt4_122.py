def add_elements(arr, k):
    # Initialize a variable to store the sum
    total_sum = 0
    
    # Iterate through the first k elements of the array
    for i in range(min(k, len(arr))):
        if 10 <= arr[i] <= 99:  # Check if the element has at most two digits
            total_sum += arr[i]  # Add the element to the sum
    
    return total_sum

# Test case
print(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4))  # Output: 24
