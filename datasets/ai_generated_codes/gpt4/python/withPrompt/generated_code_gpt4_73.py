def smallest_change(arr):
    """
    Find the minimum number of elements to change to make the array palindromic.

    Args:
    arr (list): List of integers.

    Returns:
    int: The minimum number of elements that need to be changed to make the array palindromic.

    Examples:
    >>> smallest_change([1,2,3,5,4,7,9,6])
    4
    >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
    1
    >>> smallest_change([1, 2, 3, 2, 1])
    0
    """

    # Function to check if a list is palindromic
    def is_palindromic(lst):
        return lst == lst[::-1]

    # Initialize the minimum changes counter to 0
    min_changes = 0

    # Iterate through the array and make changes if necessary
    for i in range(len(arr)):
        # Check if the array is already palindromic
        if is_palindromic(arr):
            break

        # If not palindromic, increment the minimum changes counter
        min_changes += 1

        # Make a change by replacing the current element with its complement
        arr[i] = arr[-(i + 1)]

    return min_changes
