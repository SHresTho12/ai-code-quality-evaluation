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
