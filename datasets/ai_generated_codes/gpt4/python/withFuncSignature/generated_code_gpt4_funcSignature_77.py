def iscube(a):
    """
    Checks if a given number is a perfect cube.

    :param a: The number to check.
    :return: True if 'a' is a perfect cube, False otherwise.
    """
    if a < 0:
        n = -int(abs(a) ** (1/3))
    else:
        n = int(a ** (1/3))

    return n**3 == a
