def is_simple_power(x, n):
    if n == 1 and x != 1:
        return False
    if x == 1:
        return True
    i = n
    while i <= x:
        if i == x:
            return True
        i *= n
    return False