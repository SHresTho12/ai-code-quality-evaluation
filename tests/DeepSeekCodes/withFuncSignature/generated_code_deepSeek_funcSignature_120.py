# This is a generated Python file.
def maximum(arr, k):
    if len(arr) < k:
        return None
    max_sum = current_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    return max_sum



def check(maximum):
    # Check some simple cases
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5], "Test 1"
    assert maximum([4, -4, 4], 2) == [4, 4], "Test 2"
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2], "Test 3"
    assert maximum([123, -123, 20, 0 , 1, 2, -3], 3) == [2, 20, 123], "Test 4"
    assert maximum([-123, 20, 0 , 1, 2, -3], 4) == [0, 1, 2, 20], "Test 5"
    assert maximum([5, 15, 0, 3, -13, -8, 0], 7) == [-13, -8, 0, 0, 3, 5, 15], "Test 6"
    assert maximum([-1, 0, 2, 5, 3, -10], 2) == [3, 5], "Test 7"
    assert maximum([1, 0, 5, -7], 1) == [5], "Test 8"
    assert maximum([4, -4], 2) == [-4, 4], "Test 9"
    assert maximum([-10, 10], 2) == [-10, 10], "Test 10"

    # Check the function
    check(maximum)
