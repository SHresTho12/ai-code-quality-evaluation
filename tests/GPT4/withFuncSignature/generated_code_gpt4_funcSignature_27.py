def flip_case(string: str) -> str:
    """ Return a new string with flipped case for each character in the input string. """
    return string.swapcase()

# Example usage
test_string = "Hello, World!"
result = flip_case(test_string)
result

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(flip_case): 
    assert flip_case('') == '' 
    assert flip_case('Hello!') == 'hELLO!' 
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS' 
    
check(flip_case)