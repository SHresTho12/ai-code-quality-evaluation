def monotonic(l: list):
    # Check if the list is either non-decreasing or non-increasing
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Example usage
print(monotonic([1, 2, 2, 3]))  # Output: True (non-decreasing)
print(monotonic([3, 3, 2, 1]))  # Output: True (non-increasing)
print(monotonic([1, 3, 2]))     # Output: False

METADATA = {}

def check(monotonic):
    assert monotonic([1, 2, 4, 10]) == True
    assert monotonic([1, 2, 4, 20]) == True
    assert monotonic([1, 20, 4, 10]) == False
    assert monotonic([4, 1, 0, -10]) == True
    assert monotonic([4, 1, 1, 0]) == True
    assert monotonic([1, 2, 3, 2, 5, 60]) == False
    assert monotonic([1, 2, 3, 4, 5, 60]) == True
    assert monotonic([9, 9, 9, 9]) == True

check(monotonic)
