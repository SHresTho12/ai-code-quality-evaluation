def minSubArraySum(nums):
    if not nums:
        return 0

    min_sum = float('inf')
    current_sum = 0

    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        
        # If the current sum becomes negative, reset it to 0
        if current_sum < 0:
            current_sum = 0

    return min_sum

# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))         # Output: -6
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