# This is a generated Python file.
def get_odd_collatz(n):
    count = 0
    while n != 1:
        if n % 2 != 0:
            count += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    return count