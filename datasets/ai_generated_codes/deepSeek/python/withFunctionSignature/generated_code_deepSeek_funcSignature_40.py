# This is a generated Python file.
from itertools import combinations

def triples_sum_to_zero(l: list):
    return [triple for triple in combinations(l, 3) if sum(triple) == 0]