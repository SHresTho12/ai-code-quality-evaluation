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


METADATA = {} 
def check(prime_fib): 
    assert prime_fib(1) == 2 
    assert prime_fib(2) == 3 
    assert prime_fib(3) == 5 
    assert prime_fib(4) == 13 
    assert prime_fib(5) == 89 
    assert prime_fib(6) == 233 
    assert prime_fib(7) == 1597 
    assert prime_fib(8) == 28657 
    assert prime_fib(9) == 514229 
    assert prime_fib(10) == 433494437 

check(prime_fib)