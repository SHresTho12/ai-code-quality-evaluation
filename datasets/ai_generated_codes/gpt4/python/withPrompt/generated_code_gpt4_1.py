from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Separates multiple groups of nested parentheses into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separated groups of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    cleaned_string = ''.join(paren_string.split())  # Remove spaces
    result = []
    balance = 0
    current_group = []

    for char in cleaned_string:
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            balance -= 1
            current_group.append(char)
            if balance == 0:
                result.append(''.join(current_group))
                current_group = []

    return result
