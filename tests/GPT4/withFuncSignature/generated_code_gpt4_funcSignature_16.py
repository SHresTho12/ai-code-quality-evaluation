def count_distinct_characters(string: str) -> int:
    """ Return the number of distinct characters in the given string. """
    return len(set(string))

# Testing the function
test_string = "hello world"
result = count_distinct_characters(test_string)
result



METADATA = { 'author': 'jt', 'dataset': 'test' } 

def check(count_distinct_characters): 
    assert count_distinct_characters('') == 0 
    assert count_distinct_characters('abcde') == 5 
    assert count_distinct_characters('abcde' + 'cade' + 'CADE') == 5 
    assert count_distinct_characters('aaaaAAAAaaaa') == 1 
    assert count_distinct_characters('Jerry jERRY JeRRRY') == 5 
    
check(count_distinct_characters)