# This is a generated Python file.
def largest_divisor(n: int) -> int:
    for i in range(n//2, 0, -1):
        if n % i == 0:
            return i
    return 1

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(largest_divisor): 
    assert largest_divisor(3) == 1 
    assert largest_divisor(7) == 1 
    assert largest_divisor(10) == 5 
    assert largest_divisor(100) == 50 
    assert largest_divisor(49) == 7 
    
check(largest_divisor)