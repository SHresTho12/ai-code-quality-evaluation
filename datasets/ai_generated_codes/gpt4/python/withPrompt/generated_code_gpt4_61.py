def correct_bracketing(brackets: str):
    """
    Check if the input string has correct bracketing.

    Args:
    brackets (str): A string consisting of '(' and ')'.

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, otherwise False.

    Examples:
    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    stack = []
    for char in brackets:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False  # No matching opening bracket
            stack.pop()
    return len(stack) == 0

# Example tests
print(correct_bracketing("("))       # Output: False
print(correct_bracketing("()"))      # Output: True
print(correct_bracketing("(()())"))  # Output: True
print(correct_bracketing(")(()"))    # Output: False
