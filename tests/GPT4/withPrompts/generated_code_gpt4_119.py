def match_parens(lst):
    # Join the two strings from the list
    concatenated_string = "".join(lst)

    balance = 0  # Variable to keep track of balanced parentheses

    for char in concatenated_string:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
            if balance < 0:
                return 'No'  # Unbalanced parentheses found

    if balance == 0:
        return 'Yes'  # All parentheses are balanced
    else:
        return 'No'  # Unbalanced parentheses found

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'

def check(match_parens):
    # Check some simple cases
    assert match_parens(['()(', ')']) == 'Yes', "Test 1"
    assert match_parens([')', ')']) == 'No', "Test 2"
    assert match_parens(['(()(())', '())())']) == 'No', "Test 3"
    assert match_parens([')())', '(()()(']) == 'Yes', "Test 4"
    assert match_parens(['(())))', '(()())((']) == 'Yes', "Test 5"
    assert match_parens(['()', '())']) == 'No', "Test 6"
    assert match_parens(['(()(', '()))()']) == 'Yes', "Test 7"
    assert match_parens(['((((', '((())']) == 'No', "Test 8"
    assert match_parens([')(()', '(()(']) == 'No', "Test 9"
    assert match_parens([')(', ')(']) == 'No', "Test 10"

    # Check the function
    check(match_parens)
