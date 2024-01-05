# This is a generated Python file.
def strange_sort_list(lst):
    return sorted(lst, key=lambda x: (x % 3, -x))