def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    vowel_positions = []

    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if word[i - 1] in consonants and word[i + 1] in consonants:
                return word[i]

    return ""

# Test cases
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))    # Output: "U"
print(get_closest_vowel("quick"))   # Output: ""
print(get_closest_vowel("ab"))      # Output: ""
