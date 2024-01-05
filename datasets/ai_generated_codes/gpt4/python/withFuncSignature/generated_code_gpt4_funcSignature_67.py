def fruit_distribution(s, n):
    """
    Distributes a string of fruits into 'n' groups, maintaining the order.

    :param s: A string representing fruits.
    :param n: The number of groups to divide the fruits into.
    :return: A list of strings, each representing a group of fruits.
    """
    if n <= 0:
        raise ValueError("Number of groups must be positive")

    length = len(s)
    base_size, extra = divmod(length, n)
    groups = []

    start = 0
    for i in range(n):
        group_size = base_size + (1 if i < extra else 0)
        groups.append(s[start:start + group_size])
        start += group_size

    return groups
