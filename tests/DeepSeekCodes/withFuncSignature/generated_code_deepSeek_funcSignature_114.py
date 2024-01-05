# This is a generated Python file.
def minSubArraySum(nums):
    min_ending_here = min_so_far = nums[0]
    for num in nums[1:]:
        min_ending_here = min(num, min_ending_here + num)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

def check(minSubArraySum):
    # Check some simple cases
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1, "Test 1"
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([-1, -2, -3, 2, -10]) == -14
    assert minSubArraySum([-9999999999999999]) == -9999999999999999
    assert minSubArraySum([0, 10, 20, 1000000]) == 0
    assert minSubArraySum([-1, -2, -3, 10, -5]) == -6
    assert minSubArraySum([100, -1, -2, -3, 10, -5]) == -6
    assert minSubArraySum([10, 11, 13, 8, 3, 4]) == 3
    assert minSubArraySum([100, -33, 32, -1, 0, -2]) == -33

    # Check some edge cases that are easy to work out by hand
    assert minSubArraySum([-10]) == -10, "Test 2"
    assert minSubArraySum([7]) == 7
    assert minSubArraySum([1, -1]) == -1

# Check the function
check(minSubArraySum)
