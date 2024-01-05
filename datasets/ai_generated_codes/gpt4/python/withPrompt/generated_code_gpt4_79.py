def decimal_to_binary(decimal):
    """
    Convert a decimal number to binary format.

    Args:
    decimal (int): The decimal number to be converted.

    Returns:
    str: The binary representation of the decimal number with 'db' at the beginning and end.

    Examples:
    >>> decimal_to_binary(15)
    'db1111db'
    >>> decimal_to_binary(32)
    'db100000db'
    """
    
    # Convert the decimal number to binary and remove the '0b' prefix
    binary_str = bin(decimal)[2:]
    
    # Add 'db' at the beginning and end of the binary string
    result = 'db' + binary_str + 'db'
    
    return result
