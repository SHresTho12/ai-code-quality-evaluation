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