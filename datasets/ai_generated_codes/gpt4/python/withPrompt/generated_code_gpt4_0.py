from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list first to make comparison easier
    sorted_numbers = sorted(numbers)

    # Iterate over the list and check adjacent elements
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) <= threshold:
            return True

    return False
