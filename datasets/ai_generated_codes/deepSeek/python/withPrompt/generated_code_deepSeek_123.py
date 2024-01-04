def get_odd_collatz(n):
    def collatz(n):
        while n != 1:
            yield n
            n = n * 3 + 1 if n % 2 else n // 2
        yield 1

    return sorted(x for x in collatz(n) if x % 2)