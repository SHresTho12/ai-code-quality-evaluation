def monotonic(l: list):
    # Check if the list is either non-decreasing or non-increasing
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Example usage
print(monotonic([1, 2, 2, 3]))  # Output: True (non-decreasing)
print(monotonic([3, 3, 2, 1]))  # Output: True (non-increasing)
print(monotonic([1, 3, 2]))     # Output: False
