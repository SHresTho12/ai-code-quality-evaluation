# This is a generated Python file.
from itertools import combinations

def pairs_sum_to_zero(l: list):
    return [pair for pair in combinations(l, 2) if sum(pair) == 0]