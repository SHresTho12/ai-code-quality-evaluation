
def correct_bracketing(brackets: str) -> bool:
  """
  Checks if a string of brackets is correctly balanced.

  Args:
      brackets: The string of brackets to check (str).

  Returns:
      True if the brackets are balanced, False otherwise (bool).
  """

  opening_brackets = "({["
  closing_brackets = ")}]"
  matching_brackets = {")": "(", "}": "{", "]": "["}

  stack = []

  for bracket in brackets:
    if bracket in opening_brackets:
      stack.append(bracket)
    elif bracket in closing_brackets:
      if not stack or stack.pop() != matching_brackets[bracket]:
        return False
    else:
      return False  # Invalid character

  return not stack  # True if the stack is empty (all opening brackets have matching closing brackets)

# Example usage
print(correct_bracketing("()[]{}"))  # True
print(correct_bracketing("([)]"))  # False
print(correct_bracketing("({[]})"))  # True
print(correct_bracketing(")("))  # False
print(correct_bracketing("())"))  # True
print(correct_bracketing(")(())"))  # False


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