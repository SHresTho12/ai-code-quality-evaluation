def prime_length(string):
    num = len(string)
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def check(prime_length):
    # Check some simple cases
    assert prime_length('Hello') == True, "Test 1"
    assert prime_length('abcdcba') == True, "Test 2"
    assert prime_length('kittens') == True, "Test 3"
    assert prime_length('orange') == False, "Test 4"
    assert prime_length('wow') == True, "Test 5"
    assert prime_length('world') == True, "Test 6"
    assert prime_length('MadaM') == True, "Test 7"
    assert prime_length('Wow') == True, "Test 8"
    assert prime_length('') == False, "Test 9"
    assert prime_length('HI') == True, "Test 10"
    assert prime_length('go') == True, "Test 11"
    assert prime_length('gogo') == False, "Test 12"
    assert prime_length('aaaaaaaaaaaaaaa') == False, "Test 13"

check(prime_length)
