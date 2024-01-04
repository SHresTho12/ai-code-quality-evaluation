# This is a generated Python file.
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]