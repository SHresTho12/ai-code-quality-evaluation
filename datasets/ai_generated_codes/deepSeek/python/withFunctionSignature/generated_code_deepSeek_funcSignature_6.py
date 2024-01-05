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