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