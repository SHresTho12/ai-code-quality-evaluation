def total_match(lst1, lst2):
    """
    Return the list with the total number of characters in all strings less than the other list.

    Args:
    lst1 (list): First list of strings.
    lst2 (list): Second list of strings.

    Returns:
    list: The list that has the total number of characters in all strings less than the other list.

    Examples:
    >>> total_match([], [])
    []
    >>> total_match(['hi', 'admin'], ['hI', 'Hi'])
    ['hI', 'Hi']
    >>> total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
    ['hi', 'admin']
    >>> total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])
    ['hI', 'hi', 'hi']
    >>> total_match(['4'], ['1', '2', '3', '4', '5'])
    ['4']
    """

    # Function to calculate the total number of characters in a list of strings
    def total_chars(lst):
        return sum(len(s) for s in lst)

    # Calculate the total number of characters in both lists
    total_chars_lst1 = total_chars(lst1)
    total_chars_lst2 = total_chars(lst2)

    # Compare the total number of characters and return the appropriate list
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2
