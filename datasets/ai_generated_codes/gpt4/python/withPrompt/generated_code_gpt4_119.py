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
