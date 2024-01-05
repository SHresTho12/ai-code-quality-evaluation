def correct_bracketing(brackets: str):
    """
    Check if the brackets in the input string are correctly balanced.

    Args:
    brackets (str): A string containing "<" and ">" brackets.

    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.

    Examples:
    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    stack = []  # Use a stack to keep track of opening brackets
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)  # Push opening bracket onto the stack
        elif bracket == ">":
            if not stack:
                return False  # Closing bracket with no corresponding opening bracket
            stack.pop()  # Pop the corresponding opening bracket from the stack
    
    return len(stack) == 0  # If the stack is empty, all brackets are correctly balanced

# Example tests
print(correct_bracketing("<"))       # Output: False
print(correct_bracketing("<>"))     # Output: True
print(correct_bracketing("<<><>>")) # Output: True
print(correct_bracketing("><<>"))   # Output: False
METADATA = {}

def check(correct_bracketing):
    assert correct_bracketing("<>")
    assert correct_bracketing("<<><>>")
    assert correct_bracketing("<><><<><>><>")
    assert correct_bracketing("<><><<<><><>><>><<><><<>>>")
    assert not correct_bracketing("<<<><>>>>")
    assert not correct_bracketing("><<>")
    assert not correct_bracketing("<")
    assert not correct_bracketing("<<<<")
    assert not correct_bracketing(">")
    assert not correct_bracketing("<<>")
    assert not correct_bracketing("<><><<><>><>><<>")
    assert not correct_bracketing("<><><<><>><>>><>")

check(correct_bracketing)