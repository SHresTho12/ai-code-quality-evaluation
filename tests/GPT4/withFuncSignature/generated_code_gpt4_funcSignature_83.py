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


def check(starts_one_ends):
    # Check some simple cases
    assert starts_one_ends(1) == 1, "Test 1"
    assert starts_one_ends(2) == 18, "Test 2"
    assert starts_one_ends(3) == 180, "Test 3"
    assert starts_one_ends(4) == 1800, "Test 4"
    assert starts_one_ends(5) == 18000, "Test 5"

check(starts_one_ends)