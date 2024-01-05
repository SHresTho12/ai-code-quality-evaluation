def pairs_sum_to_zero(l):
    num_set = set()
    for num in l:
        if -num in num_set:
            return True
        num_set.add(num)
    return False