# This is a generated Python file.
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors