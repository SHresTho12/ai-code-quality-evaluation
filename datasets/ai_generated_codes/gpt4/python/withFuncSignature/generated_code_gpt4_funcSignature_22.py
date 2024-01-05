from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

# Example usage
test_values = [1, 2, "a", "b", 3, 4.5, 5]
result = filter_integers(test_values)
result
