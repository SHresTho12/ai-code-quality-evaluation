def match_parens(lst):
    def is_balanced(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    for perm in [''.join(p) for p in permutations(lst)]:
        if is_balanced(perm):
            return 'Yes'
    return 'No'


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

