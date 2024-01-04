
def match_parens(lst):
  """
  Checks if the parentheses in a list are balanced.

  Args:
    lst: A list of characters.

  Returns:
    True if the parentheses are balanced, False otherwise.
  """

  stack = []
  for char in lst:
    if char == "(":
      stack.append(char)
    elif char == ")":
      if not stack or stack.pop() != "(":
        return False
  return not stack

# Example usage
lst1 = ["(", "a", "(", "b", ")", ")", "c"]  # True
lst2 = ["(", "a", "b", ")", "c"]  # False
lst3 = [")", "a", "(", "b", ")"]  # False

print(f"List 1: {lst1} - Balanced? {match_parens(lst1)}")
print(f"List 2: {lst2} - Balanced? {match_parens(lst2)}")
print(f"List 3: {lst3} - Balanced? {match_parens(lst3)}")
