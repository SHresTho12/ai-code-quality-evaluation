# This is a generated Python file.
from typing import List


def sort_numbers(numbers: str) -> str:
    return ' '.join(sorted(numbers.split(), key=int))


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(sort_numbers): 
    assert sort_numbers('') == '' 
    assert sort_numbers('three') == 'three' 
    assert sort_numbers('three five nine') == 'three five nine' 
    assert sort_numbers('five zero four seven nine eight') == 'zero four five seven eight nine' 
    assert sort_numbers('six five four three two one zero') == 'zero one two three four five six' 
    
check(sort_numbers)
