def minSubArraySum(nums):
    curr_min = nums[0]
    global_min = nums[0]
    for i in range(1, len(nums)):
        curr_min = min(nums[i], curr_min + nums[i])
        global_min = min(global_min, curr_min)
    return global_min