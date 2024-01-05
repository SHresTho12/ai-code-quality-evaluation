def below_threshold(l: list, t: int):
    """
    Returns a list of elements from the input list 'l' that are below the threshold 't'.

    :param l: A list of integers.
    :param t: An integer threshold value.
    :return: A list of integers from 'l' that are less than 't'.
    """
    return [element for element in l if element < t]
