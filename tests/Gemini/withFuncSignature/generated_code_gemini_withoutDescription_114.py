
def minSubArraySum(nums):
  """
  Finds the minimum sum of a contiguous subarray in a given array.

  Args:
    nums: A list of integers.

  Returns:
    The minimum sum of any contiguous subarray in nums.
  """

  min_sum = float('inf')  # Initialize minimum sum to infinity
  current_sum = 0

  for num in nums:
    current_sum += num  # Add the current number to the current sum
    min_sum = min(min_sum, current_sum)  # Update minimum sum if necessary

    # If the current sum becomes negative, reset it to 0 for a fresh start
    # This is because a negative current sum can only worsen the minimum sum
    if current_sum < 0:
      current_sum = 0

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
