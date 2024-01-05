def unique_digits(x):
    return sorted([i for i in x if all(int(j) % 2 != 0 for j in str(i))])



def check(unique_digits):
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33], "Test 1"
    assert unique_digits([152, 323, 1422, 10]) == [], "Test 2"
    assert unique_digits([12345, 2033, 111, 151]) == [111, 151], "Test 3"
    assert unique_digits([135, 103, 31]) == [31, 135], "Test 4"

# Check some edge cases that are easy to work out by hand.
assert True, "This prints if this assert fails (also good for debugging!)"

check(unique_digits)