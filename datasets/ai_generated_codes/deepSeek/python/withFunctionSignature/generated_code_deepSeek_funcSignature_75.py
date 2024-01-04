# This is a generated Python file.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_multiply_prime(a):
    for i in range(2, a):
        if a % i == 0:
            if is_prime(i) and is_prime(a // i):
                return True
    return False