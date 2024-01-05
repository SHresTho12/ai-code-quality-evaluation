def select_words(s, n):
    vowels = 'aeiouAEIOU'
    words = s.split()
    result = []
    for word in words:
        count = sum(1 for c in word if c not in vowels)
        if count == n:
            result.append(word)
    return result


def check(select_words):
    # Check some simple cases
    assert select_words("Mary had a little lamb", 4) == ["little"], "Test 1"
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"], "Test 2"
    assert select_words("simple white space", 2) == [], "Test 3"
    assert select_words("Hello world", 4) == ["world"], "Test 4"
    assert select_words("Uncle sam", 3) == ["Uncle"], "Test 5"

    # Check some edge cases that are easy to work out by hand.
    assert select_words("", 4) == [], "Test 6"
    assert select_words("a b c d e f", 1) == ["b", "c", "d", "f"], "Test 7"

    # Check the function
    check(select_words)