def correct_bracketing(brackets: str):
    """
    Checks if a string of brackets is correctly bracketed.

    :param brackets: A string consisting of brackets (e.g., '()', '{}', '[]').
    :return: True if the bracketing is correct, False otherwise.
    """
    stack = []
    opening_brackets = {'(', '{', '['}
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in matching_brackets:
            if not stack or stack[-1] != matching_brackets[bracket]:
                return False
            stack.pop()
        else:
            # Invalid character
            return False

    return len(stack) == 0
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