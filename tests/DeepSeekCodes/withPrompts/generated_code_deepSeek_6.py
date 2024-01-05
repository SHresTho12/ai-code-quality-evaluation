from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    max_depths = []
    for group in groups:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif char == ')':
                depth -= 1
        max_depths.append(max_depth)
    return max_depths


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(parse_nested_parens): 
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3] 
    assert parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4] 
    assert parse_nested_parens('(()(())((())))') == [4] 
    
check(parse_nested_parens)