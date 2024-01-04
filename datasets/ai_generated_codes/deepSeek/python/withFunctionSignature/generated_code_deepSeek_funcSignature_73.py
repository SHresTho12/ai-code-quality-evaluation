# This is a generated Python file.
def smallest_change(arr):
    changes = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    return min(changes)