def multiply(a, b):
    # Get the unit digits of both numbers
    unit_a = abs(a) % 10
    unit_b = abs(b) % 10

    # Calculate the product of unit digits
    result = unit_a * unit_b

    return result

# Test cases
print(multiply(148, 412))     # Output: 16
print(multiply(19, 28))       # Output: 72
print(multiply(2020, 1851))   # Output: 0
print(multiply(14, -15))      # Output: 20
