from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []

    min_num = min(numbers)
    max_num = max(numbers)

    # Handle the case where all numbers are the same
    if min_num == max_num:
        return [1.0 for _ in numbers]

    range_num = max_num - min_num
    return [(num - min_num) / range_num for num in numbers]

# Example usage
test_numbers = [10, 15, 20, 25, 30]
result = rescale_to_unit(test_numbers)
result
