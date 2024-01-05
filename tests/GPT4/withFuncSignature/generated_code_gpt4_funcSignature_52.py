def below_threshold(l: list, t: int):
    """
    Returns a list of elements from the input list 'l' that are below the threshold 't'.

    :param l: A list of integers.
    :param t: An integer threshold value.
    :return: A list of integers from 'l' that are less than 't'.
    """
    return [element for element in l if element < t]
METADATA = {}

def check(below_threshold):
    assert below_threshold([1, 2, 4, 10], 100)
    assert not below_threshold([1, 20, 4, 10], 5)
    assert below_threshold([1, 20, 4, 10], 21)
    assert below_threshold([1, 20, 4, 10], 22)
    assert below_threshold([1, 8, 4, 10], 11)
    assert not below_threshold([1, 8, 4, 10], 10)

check(below_threshold)