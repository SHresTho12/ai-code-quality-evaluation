def smallest_change(arr):
    """
    Finds the smallest amount of money that cannot be formed with the denominations in the array.

    :param arr: An array of integers representing the denominations.
    :return: The smallest amount of money that cannot be formed.
    """
    arr.sort()
    current_change = 0

    for coin in arr:
        if coin > current_change + 1:
            break
        current_change += coin

    return current_change + 1
