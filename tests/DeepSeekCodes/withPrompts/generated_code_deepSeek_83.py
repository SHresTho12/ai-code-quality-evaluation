def starts_one_ends(n):
    if n == 1:
        return 2
    else:
        return 10**(n-1)*2
    

def check(starts_one_ends):
    # Check some simple cases
    assert starts_one_ends(1) == 1, "Test 1"
    assert starts_one_ends(2) == 18, "Test 2"
    assert starts_one_ends(3) == 180, "Test 3"
    assert starts_one_ends(4) == 1800, "Test 4"
    assert starts_one_ends(5) == 18000, "Test 5"

check(starts_one_ends)