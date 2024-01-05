from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            if stack:
                current_group += char
            stack.append(char)
        elif char == ')':
            if stack:
                current_group += char
                stack.pop()
                if not stack:
                    result.append(current_group)
                    current_group = ""
            else:
                # Handle unmatched closing parenthesis if needed
                pass
        elif stack:
            current_group += char

    # Handle any unmatched opening parenthesis if needed

    return result
