def sort_array(array):
    if not array:
        return []
    new_array = array.copy()
    if (array[0] + array[-1]) % 2 == 0:
        new_array.sort(reverse=True)
    else:
        new_array.sort()
    return new_array