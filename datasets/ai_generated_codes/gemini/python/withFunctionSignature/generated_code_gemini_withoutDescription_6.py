
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parses a string with nested parentheses and extracts the numbers within them,
    preserving their nesting structure as a list of integers.

    Args:
        paren_string: The input string containing parentheses and numbers.

    Returns:
        A list of integers, where each integer represents a nested level of parentheses,
        with the innermost level as 0 and increasing outward.
    """

    result = []
    current_level = 0

    for char in paren_string:
        if char == "(":
            current_level += 1
            result.append(current_level)
        elif char == ")":
            current_level -= 1
        else:
            try:
                num = int(char)
                result.append(current_level + num)  # Add number relative to current level
            except ValueError:
                pass  # Ignore non-numeric characters

    return result
