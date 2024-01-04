# This is a generated Python file.
def maximum(arr, k):
    if len(arr) < k:
        return None
    max_sum = current_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    return max_sum