def change_base(x: int, base: int):
    # Validate the base
    if base < 2 or base > 10:
        return "Invalid base. Base must be between 2 and 10."

    # Handle the case for zero
    if x == 0:
        return "0"

    # Convert x to a positive number and remember if it was negative
    negative = False
    if x < 0:
        negative = True
        x = -x

    # Convert the number
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base

    # If the original number was negative, add the negative sign
    if negative:
        return '-' + ''.join(reversed(digits))
    
    return ''.join(reversed(digits))

# Example usage
print(change_base(345, 2))  # Output: The binary representation of 345
print(change_base(128, 8))  # Output: The octal representation of 128


METADATA = {} 
def check(change_base): 
    assert change_base(8, 3) == "22" 
    assert change_base(9, 3) == "100" 
    assert change_base(234, 2) == "11101010" 
    assert change_base(16, 2) == "10000" 
    assert change_base(8, 2) == "1000" 
    assert change_base(7, 2) == "111" 
    for x in range(2, 8): 
        assert change_base(x, x + 1) == str(x) 
        
check(change_base)