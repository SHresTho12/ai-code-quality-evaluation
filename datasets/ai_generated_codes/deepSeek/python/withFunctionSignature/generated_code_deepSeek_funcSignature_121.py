# This is a generated Python file.
def solution(lst):
    result = []
    for s in set(lst):
        result.append((s, lst.count(s)))
    return result