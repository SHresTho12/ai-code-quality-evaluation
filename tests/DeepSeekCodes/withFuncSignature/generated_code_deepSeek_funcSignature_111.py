# This is a generated Python file.
def histogram(test):
    hist = {}
    for char in test:
        if char in hist:
            hist[char] += 1
        else:
            hist[char] = 1
    return hist

def check(histogram):
    # Check some simple cases
    assert histogram('a b b a') == {'a': 2, 'b': 2}, "Test 1"
    assert histogram('a b c a b') == {'a': 2, 'b': 2, 'c': 1}, "Test 2"
    assert histogram('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, "Test 3"
    assert histogram('r t g') == {'r': 1, 't': 1, 'g': 1}, "Test 4"
    assert histogram('b b b b a') == {'b': 4, 'a': 1}, "Test 5"
    
    # Check some edge cases that are easy to work out by hand.
    assert histogram('') == {}, "Test 6"
    assert histogram('a') == {'a': 1}, "Test 7"

check(histogram)
