# This is a generated Python file.
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    groups = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            group = ''
            while stack and stack[-1] != '(':
                group = stack.pop() + group
            if stack and stack[-1] == '(':
                stack.pop()
            groups.append(group)
    return groups

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(separate_paren_groups): 
    assert separate_paren_groups('(()()) ((())) () ((())()())') == [ '(()())', '((()))', '()', '((())()())' ] 
    assert separate_paren_groups('() (()) ((())) (((())))') == [ '()', '(())', '((()))', '(((())))' ] 
    assert separate_paren_groups('(()(())((())))') == [ '(()(())((())))' ] 
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'] 
    

check(separate_paren_groups)