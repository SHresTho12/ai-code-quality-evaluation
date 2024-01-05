
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separates a string containing parentheses into a list of substrings,
    where each substring is a group of characters enclosed within a matching pair of parentheses.

    Args:
        paren_string: The input string containing parentheses.

    Returns:
        A list of substrings, where each substring is a group of characters enclosed within matching parentheses.
    """

    groups = []
    current_group = ""
    level = 0

    for char in paren_string:
        if char == "(":
            level += 1
            if level > 1:
                current_group += char
        elif char == ")":
            level -= 1
            if level == 0:
                groups.append(current_group)
                current_group = ""
            else:
                current_group += char
        else:
            current_group += char

    if current_group:
        groups.append(current_group)  # Add any remaining group at the end

    return groups

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(separate_paren_groups): 
    assert separate_paren_groups('(()()) ((())) () ((())()())') == [ '(()())', '((()))', '()', '((())()())' ] 
    assert separate_paren_groups('() (()) ((())) (((())))') == [ '()', '(())', '((()))', '(((())))' ] 
    assert separate_paren_groups('(()(())((())))') == [ '(()(())((())))' ] 
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())'] 
    

check(separate_paren_groups)