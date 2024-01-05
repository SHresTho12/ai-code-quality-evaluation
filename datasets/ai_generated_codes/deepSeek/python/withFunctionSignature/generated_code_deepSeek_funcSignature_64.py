# This is a generated Python file.
def vowels_count(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count