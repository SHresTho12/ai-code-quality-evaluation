def remove_vowels(text):
    # Define the vowels
    vowels = "aeiouAEIOU"
    
    # Use a list comprehension to filter out the vowels and join the remaining characters
    return ''.join(char for char in text if char not in vowels)

# Example usage
print(remove_vowels("Hello World"))  # Output: "Hll Wrld"
METADATA = {}

def check(remove_vowels):
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('fedcba') == 'fdcb'
    assert remove_vowels('eeeee') == ''
    assert remove_vowels('acBAA') == 'cB'
    assert remove_vowels('EcBOO') == 'cB'
    assert remove_vowels('ybcd') == 'ybcd'

check(remove_vowels)