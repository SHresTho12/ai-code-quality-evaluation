from typing import List

def sort_numbers(numbers: str) -> str:
    """Sort a space-delimited string of numerals from smallest to largest.

    Args:
    numbers (str): A space-delimited string of numerals ('zero' to 'nine').

    Returns:
    str: The string with numbers sorted from smallest to largest.

    Examples:
    >>> sort_numbers('three one five')
    'one three five'
    """
    numeral_to_int = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    int_to_numeral = {v: k for k, v in numeral_to_int.items()}

    numeral_list = numbers.split()
    sorted_numerals = sorted(numeral_list, key=lambda x: numeral_to_int[x])
    return ' '.join(sorted_numerals)

