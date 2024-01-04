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

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def prime_fib(n: int):
    count = 0
    i = 0
    while count < n:
        fib_num = fib(i)
        if is_prime(fib_num):
            count += 1
        i += 1
    return fib(i - 1)