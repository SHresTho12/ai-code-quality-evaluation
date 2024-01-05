# This is a generated Python file.
def get_closest_vowel(word):
    vowels = 'aeiou'
    first_vowel = next((c for c in word if c in vowels), None)
    if first_vowel is None:
        return None
    return min(vowels, key=lambda v: abs(ord(v) - ord(first_vowel)))