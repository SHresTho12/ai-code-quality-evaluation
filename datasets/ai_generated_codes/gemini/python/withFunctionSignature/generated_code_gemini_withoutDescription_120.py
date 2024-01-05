
def maximum(arr, k):
    """
    Finds the maximum of k numbers in an array.

    Args:
        arr: A list of numbers.
        k: The number of largest elements to find.

    Returns:
        A list containing the k largest elements in the array, in descending order.
    """

    # Handle cases where k is invalid or the array is empty
    if k <= 0 or not arr:
        return []

    # Sort the array in descending order to efficiently find the largest elements
    arr.sort(reverse=True)

    # Return the first k elements of the sorted array, which are the k largest
    return arr[:k]
