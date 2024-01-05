from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depth = 0
    depth_list = []

    for char in paren_string:
        if char == '(':
            depth += 1
            depth_list.append(depth)
        elif char == ')':
            depth_list.append(depth)
            depth -= 1
        else:
            depth_list.append(depth)

    return depth_list

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(parse_nested_parens): 
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3] 
    assert parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4] 
    assert parse_nested_parens('(()(())((())))') == [4] 
    
check(parse_nested_parens)