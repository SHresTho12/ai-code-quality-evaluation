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
