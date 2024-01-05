def decimal_to_binary(decimal):
    """
    Converts a decimal number to its binary representation using Python's built-in function.

    :param decimal: The decimal number to convert.
    :return: A string representing the binary form of the decimal number.
    """
    # The bin function returns a string like '0b101', so we slice to remove the '0b' prefix
    return bin(decimal)[2:]
