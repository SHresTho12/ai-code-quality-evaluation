from typing import List

def below_zero(operations: List[int]) -> bool:
    total = 0
    for op in operations:
        total += op
        if total < 0:
            return True
    return False
