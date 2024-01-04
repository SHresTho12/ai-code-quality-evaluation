def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join([ch for ch in text if ch not in vowels])