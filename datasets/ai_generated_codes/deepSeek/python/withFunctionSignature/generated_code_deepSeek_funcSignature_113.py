# This is a generated Python file.
def odd_count(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return [num for num, count in count_dict.items() if count % 2 == 1]