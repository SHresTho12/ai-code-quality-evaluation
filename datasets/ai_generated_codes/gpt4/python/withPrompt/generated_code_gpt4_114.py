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
