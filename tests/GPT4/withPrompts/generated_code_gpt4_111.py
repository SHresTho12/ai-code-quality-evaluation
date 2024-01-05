def histogram(test):
    # Split the input string into a list of lowercase letters
    letters = test.split()

    # Create an empty dictionary to store letter counts
    letter_count = {}

    # Iterate through the letters and count their occurrences
    for letter in letters:
        letter = letter.lower()  # Convert to lowercase
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Find the maximum count
    max_count = max(letter_count.values())

    # Create a dictionary to store letters with the maximum count
    result = {letter: count for letter, count in letter_count.items() if count == max_count}

    return result

# Test cases
print(histogram('a b c'))      # Output: {'a': 1, 'b': 1, 'c': 1}
print(histogram('a b b a'))    # Output: {'a': 2, 'b': 2}
print(histogram('a b c a b'))  # Output: {'a': 2, 'b': 2}
print(histogram('b b b b a'))  # Output: {'b': 4}
print(histogram(''))            # Output: {}
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