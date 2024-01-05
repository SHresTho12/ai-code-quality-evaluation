from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    else:
        max_numbers = [numbers[0]]
        for num in numbers[1:]:
            max_numbers.append(max(max_numbers[-1], num))
        return max_numbers