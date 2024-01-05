from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Return a list of strings from the input list that start with the given prefix. """
    return [s for s in strings if s.startswith(prefix)]

# Example usage
test_strings = ["apple", "banana", "apricot", "cherry", "blueberry"]
test_prefix = "ap"
result = filter_by_prefix(test_strings, test_prefix)
result



METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(filter_by_prefix): 
    assert filter_by_prefix([], 'john') == [] 
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx'] 
    
check(filter_by_prefix)