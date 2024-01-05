def prime_length(string):
    num = len(string)
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True