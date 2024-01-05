def get_closest_vowel(word):
    """
    Finds the vowel in a word that is closest to the beginning of the alphabet.

    :param word: The input word.
    :return: The closest vowel found in the word.
    """
    # Define a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize variables to store the closest vowel and its position
    closest_vowel = None
    closest_position = float('inf')  # Initialize to positive infinity

    # Convert the word to lowercase for case-insensitive comparison
    word = word.lower()

    # Iterate through the characters in the word
    for i, char in enumerate(word):
        if char in vowels:
            # Calculate the distance of the current vowel from 'a' in the alphabet
            distance = ord(char) - ord('a')
            if distance < closest_position:
                closest_position = distance
                closest_vowel = char

    return closest_vowel


def check(get_closest_vowel):
    # Check some simple cases
    assert get_closest_vowel("yogurt") == "u", "Test 1"
    assert get_closest_vowel("full") == "u", "Test 2"
    assert get_closest_vowel("easy") == "", "Test 3"
    assert get_closest_vowel("eAsy") == "", "Test 4"
    assert get_closest_vowel("ali") == "", "Test 5"
    assert get_closest_vowel("bad") == "a", "Test 6"
    assert get_closest_vowel("most") == "o", "Test 7"
    assert get_closest_vowel("ab") == "", "Test 8"
    assert get_closest_vowel("ba") == "", "Test 9"
    assert get_closest_vowel("quick") == "", "Test 10"
    assert get_closest_vowel("anime") == "i", "Test 11"
    assert get_closest_vowel("Asia") == "", "Test 12"
    assert get_closest_vowel("Above") == "o", "Test 13"

# Check the function
check(get_closest_vowel)