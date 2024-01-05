# This is a generated Python file.
def match_parens(lst):
    result = []
    for s in lst:
        stack = []
        count = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    count += 1
        count += len(stack)
        result.append((s, count))
    return result



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
