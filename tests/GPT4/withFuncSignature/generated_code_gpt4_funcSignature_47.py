def median(l: list):
    # Check if the list is empty
    if not l:
        return "The list is empty."

    # Sort the list
    sorted_list = sorted(l)

    n = len(sorted_list)

    # Find the median
    if n % 2 == 0:  # If the list has an even number of elements
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:  # If the list has an odd number of elements
        return sorted_list[n // 2]

# Example usage
print(median([3, 1, 2]))  # Output: 2
print(median([3, 1, 2, 4]))  # Output: 2.5

METADATA = {} 
def check(median): 
    assert median([3, 1, 2, 4, 5]) == 3 
    assert median([-10, 4, 6, 1000, 10, 20]) == 8.0 
    assert median([5]) == 5 
    assert median([6, 5]) == 5.5 
    assert median([8, 1, 3, 9, 9, 2, 7]) == 7 
    
check(median)