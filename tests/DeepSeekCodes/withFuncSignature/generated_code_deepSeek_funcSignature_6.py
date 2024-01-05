# This is a generated Python file.
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    depths = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
            depths.append(len(stack) - 1)
        elif char == ')':
            stack.pop()
    return depths   


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(parse_nested_parens): 
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3] 
    assert parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4] 
    assert parse_nested_parens('(()(())((())))') == [4] 
    
check(parse_nested_parens)
