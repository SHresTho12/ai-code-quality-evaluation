from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    # Sort the list to simplify finding the closest elements
    sorted_numbers = sorted(numbers)

    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    min_difference = abs(sorted_numbers[1] - sorted_numbers[0])

    for i in range(1, len(sorted_numbers) - 1):
        current_difference = abs(sorted_numbers[i + 1] - sorted_numbers[i])
        if current_difference < min_difference:
            min_difference = current_difference
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair

# Example usage
test_numbers = [3.1, 4.5, 1.2, 2.8, 3.5]
result = find_closest_elements(test_numbers)

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(find_closest_elements): 
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0) 
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9) 
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2) 
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0) 
    assert find_closest_elements([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1) 
    
check(find_closest_elements)