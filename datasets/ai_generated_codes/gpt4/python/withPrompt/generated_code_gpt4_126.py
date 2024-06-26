def is_sorted(lst):
    # Check if the list is sorted in ascending order
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    
    # Check for duplicates
    unique_set = set(lst)
    for num in unique_set:
        if lst.count(num) > 1:
            return False
    
    return True

# Test cases
print(is_sorted([5]))                        # True
print(is_sorted([1, 2, 3, 4, 5]))            # True
print(is_sorted([1, 3, 2, 4, 5]))            # False
print(is_sorted([1, 2, 3, 4, 5, 6]))         # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))      # True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))      # False
print(is_sorted([1, 2, 2, 3, 3, 4]))         # True
print(is_sorted([1, 2, 2, 2, 3, 4]))         # False
