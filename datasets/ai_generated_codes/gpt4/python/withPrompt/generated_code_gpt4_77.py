def iscube(a):
    """
    Return True if the integer a is a cube of some integer number, False otherwise.

    Args:
    a (int): The input integer.

    Returns:
    bool: True if a is a cube of some integer, False otherwise.

    Examples:
    >>> iscube(1)
    True
    >>> iscube(2)
    False
    >>> iscube(-1)
    True
    >>> iscube(64)
    True
    >>> iscube(0)
    True
    >>> iscube(180)
    False
    """
    
    # Calculate the cube root of the absolute value of a
    cube_root = abs(a) ** (1/3)

    # Check if the cube root is an integer
    return cube_root.is_integer()
