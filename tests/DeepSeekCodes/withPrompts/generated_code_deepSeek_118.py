def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    return ''


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