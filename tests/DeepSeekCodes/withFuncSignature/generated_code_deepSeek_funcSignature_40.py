# This is a generated Python file.
from itertools import combinations


def triples_sum_to_zero(l: list):
    return [triple for triple in combinations(l, 3) if sum(triple) == 0]


METADATA = {} 
def check(triples_sum_to_zero): 
    assert triples_sum_to_zero([1, 3, 5, 0]) == False 
    assert triples_sum_to_zero([1, 3, 5, -1]) == False 
    assert triples_sum_to_zero([1, 3, -2, 1]) == True 
    assert triples_sum_to_zero([1, 2, 3, 7]) == False 
    assert triples_sum_to_zero([1, 2, 5, 7]) == False 
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True 
    assert triples_sum_to_zero([1]) == False 
    assert triples_sum_to_zero([1, 3, 5, -100]) == False 
    assert triples_sum_to_zero([100, 3, 5, -100]) == False 
    
check(triples_sum_to_zero)