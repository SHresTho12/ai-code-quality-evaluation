def minSubArraySum(nums):
    """
    Finds the minimum sum of any subarray in a list of numbers.

    :param nums: The list of numbers.
    :return: The minimum subarray sum.
    """
    if not nums:
        return 0
    
    # Initialize variables to keep track of the minimum sum and the current sum
    min_sum = float('inf')  # Initialize to positive infinity
    current_sum = 0
    
    # Iterate through the list of numbers
    for num in nums:
        # Update the current sum by adding the current number
        current_sum += num
        
        # If the current sum becomes negative, reset it to 0
        if current_sum < 0:
            current_sum = 0
        
        # Update the minimum sum if the current sum is smaller
        min_sum = min(min_sum, current_sum)
    
    return min_sum


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