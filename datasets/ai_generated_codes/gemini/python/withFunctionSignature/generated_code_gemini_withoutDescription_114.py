
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
