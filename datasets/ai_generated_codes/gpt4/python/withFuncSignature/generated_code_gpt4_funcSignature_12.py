from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # Check if the list is empty
        return None

    return max(strings, key=len)
