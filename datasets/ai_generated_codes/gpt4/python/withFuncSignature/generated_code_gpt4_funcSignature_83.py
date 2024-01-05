def starts_one_ends(n):
    # List to store numbers that start and end with 1
    result = []

    # Iterate through the range from 1 to n
    for num in range(1, n + 1):
        num_str = str(num)
        # Check if the number starts and ends with 1
        if num_str.startswith('1') and num_str.endswith('1'):
            result.append(num)

    return result

# Example usage
print(starts_one_ends(30))  # Output: [11]
