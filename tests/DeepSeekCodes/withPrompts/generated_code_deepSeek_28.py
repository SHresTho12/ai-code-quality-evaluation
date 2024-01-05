from typing import List


def concatenate(strings: List[str]) -> str:
    return ''.join(strings)


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(concatenate): 
    assert concatenate([]) == '' 
    assert concatenate(['x', 'y', 'z']) == 'xyz' 
    assert concatenate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk' 
    
check(concatenate)