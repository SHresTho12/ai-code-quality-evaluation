def maximum(arr, k):
    arr.sort(reverse=True)
    return sorted(arr[:k])