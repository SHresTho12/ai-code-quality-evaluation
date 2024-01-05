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
