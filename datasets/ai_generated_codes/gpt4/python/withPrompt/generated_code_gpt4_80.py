def is_happy(s):
    """
    Check if a string is happy.

    Args:
    s (str): The input string.

    Returns:
    bool: True if the string is happy, False otherwise.

    Examples:
    >>> is_happy('a')
    False
    >>> is_happy('aa')
    False
    >>> is_happy('abcd')
    True
    >>> is_happy('aabb')
    False
    >>> is_happy('adb')
    True
    >>> is_happy('xyy')
    False
    """
    
    # Check if the length of the string is at least 3
    if len(s) < 3:
        return False
    
    # Iterate through the string with a step of 3
    for i in range(0, len(s) - 2, 3):
        # Check if the current 3 consecutive letters are distinct
        if s[i] == s[i+1] or s[i] == s[i+2] or s[i+1] == s[i+2]:
            return False
    
    # If all 3 consecutive letters are distinct for the entire string, it's happy
    return True
