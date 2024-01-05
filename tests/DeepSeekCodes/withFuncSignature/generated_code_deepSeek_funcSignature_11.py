# This is a generated Python file.
from typing import List


def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(string_xor): 
    assert string_xor('111000', '101010') == '010010' 
    assert string_xor('1', '1') == '0' 
    assert string_xor('0101', '0000') == '0101' 
    
check(string_xor)