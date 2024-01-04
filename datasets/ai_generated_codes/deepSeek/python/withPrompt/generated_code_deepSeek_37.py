def sort_even(l: list):
    even_elements = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    result = l.copy()
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even_elements.pop(0)
    return result