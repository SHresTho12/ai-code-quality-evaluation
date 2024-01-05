def sort_third(l: list):
    third_elements = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    result = l.copy()
    for i in range(len(l)):
        if i % 3 == 0:
            result[i] = third_elements.pop(0)
    return result