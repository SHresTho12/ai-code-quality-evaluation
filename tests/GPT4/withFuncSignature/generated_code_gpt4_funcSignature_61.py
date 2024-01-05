def correct_bracketing(brackets: str):
    # Initialize a counter for the balance of brackets
    balance = 0

    # Iterate through each character in the string
    for char in brackets:
        if char == '(':
            # Increment balance for an opening bracket
            balance += 1
        elif char == ')':
            # Decrement balance for a closing bracket
            if balance == 0:
                # A closing bracket without a matching opening bracket
                return False
            balance -= 1

    # If balance is zero, all brackets are correctly closed
    return balance == 0

# Example usage
print(correct_bracketing("(()())"))  # Output: True
print(correct_bracketing("(()"))     # Output: False
print(correct_bracketing("())"))     # Output: False
METADATA = {}

def check(correct_bracketing):
    assert correct_bracketing("()")
    assert correct_bracketing("(()())")
    assert correct_bracketing("()()(()())()")
    assert correct_bracketing("()()((()()())())(()()(()))")
    assert not correct_bracketing("((()())))")
    assert not correct_bracketing(")(()")
    assert not correct_bracketing("(")
    assert not correct_bracketing("((((")
    assert not correct_bracketing(")")
    assert not correct_bracketing("(()")
    assert not correct_bracketing("()()(()())())(()")
    assert not correct_bracketing("()()(()())()))()")

check(correct_bracketing)