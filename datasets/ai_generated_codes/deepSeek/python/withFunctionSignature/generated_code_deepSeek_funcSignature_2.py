# This is a generated Python file.
import math

def truncate_number(number: float) -> float:
    if number >= 0:
        return math.floor(number)
    else:
        return math.ceil(number)