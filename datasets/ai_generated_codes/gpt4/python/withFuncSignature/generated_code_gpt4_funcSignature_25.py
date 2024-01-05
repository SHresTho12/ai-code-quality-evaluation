from typing import List

def factorize(n: int) -> List[int]:
    # A list to store the factors
    factors = []

    # Check every number from 1 to n (inclusive)
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors

# Example usage
result = factorize(12)  # Should return [1, 2, 3, 4, 6, 12]
result
