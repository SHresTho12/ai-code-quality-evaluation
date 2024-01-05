def exchange(lst1, lst2):
    """
    Exchanges the contents of two lists.

    :param lst1: The first list.
    :param lst2: The second list.
    """
    lst1[:], lst2[:] = lst2[:], lst1[:]
