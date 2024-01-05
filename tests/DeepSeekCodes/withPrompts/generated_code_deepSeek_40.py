def triples_sum_to_zero(l: list):
    l.sort()
    for i in range(len(l) - 2):
        left = i + 1
        right = len(l) - 1
        while left < right:
            current_sum = l[i] + l[left] + l[right]
            if current_sum == 0:
                return True
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return False

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