# This is a generated Python file.
def flip_case(string: str) -> str:
    return string.swapcase()

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(flip_case): 
    assert flip_case('') == '' 
    assert flip_case('Hello!') == 'hELLO!' 
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS' 
    
check(flip_case)