def select_words(s, n):
    def count_consonants(word):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for letter in word if letter in consonants)

    words = s.split()
    selected_words = [word for word in words if count_consonants(word) == n]

    return selected_words

# Test cases
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))  # Output: []
print(select_words("Hello world", 4))  # Output: ["world"]
print(select_words("Uncle sam", 3))  # Output: ["Uncle"]
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