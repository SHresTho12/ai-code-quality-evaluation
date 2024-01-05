def any_int(x, y, z):
    """
    Checks if any of the given arguments is an integer.

    :param x: The first argument.
    :param y: The second argument.
    :param z: The third argument.
    :return: True if any of the arguments is an integer, False otherwise.
    """
    return isinstance(x, int) or isinstance(y, int) or isinstance(z, int)
