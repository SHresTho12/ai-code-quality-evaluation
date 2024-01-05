def unique_digits(x):
    # Initialize an empty list to store unique elements without even digits
    result = []
    
    # Iterate through the elements in the input list
    for num in x:
        # Convert the number to a string to easily check its digits
        num_str = str(num)
        
        # Flag to check if the number has any even digit
        has_even_digit = False
        
        # Iterate through the digits of the number
        for digit in num_str:
            if int(digit) % 2 == 0:
                has_even_digit = True
                break
        
        # If the number has no even digit, add it to the result list
        if not has_even_digit:
            result.append(num)
    
    # Sort the result list in increasing order
    result.sort()
    
    return result

# Test cases
print(unique_digits([15, 33, 1422, 1]))    # Output: [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # Output: []
