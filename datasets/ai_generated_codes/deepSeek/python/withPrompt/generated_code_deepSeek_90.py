def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        lst = sorted(set(lst))
        return lst[1] if len(lst) > 1 else None