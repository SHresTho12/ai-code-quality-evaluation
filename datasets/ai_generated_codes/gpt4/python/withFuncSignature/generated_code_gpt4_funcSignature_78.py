def hex_key(num):
    # Convert the number to hexadecimal and return the string without the '0x' prefix
    return hex(num)[2:]

# Example usage
print(hex_key(255))  # Output: 'ff'
print(hex_key(16))   # Output: '10'
print(hex_key(10))   # Output: 'a'
