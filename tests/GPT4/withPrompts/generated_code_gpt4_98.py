def count_upper(s):
    # Initialize a count variable to keep track of uppercase vowels
    count = 0

    # Iterate through even indices of the string
    for i in range(0, len(s), 2):
        # Check if the character at the current index is an uppercase vowel
        if s[i].isupper() and s[i] in "AEIOU":
            count += 1

    return count

# Test cases
print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg')) # Output: 0
print(count_upper('dBBE'))    # Output: 0

def check(count_upper):
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
    assert count_upper('B') == 0
    assert count_upper('U') == 1
    assert count_upper('') == 0
    assert count_upper('EEEE') == 2

# Check some edge cases that are easy to work out by hand.
assert True

check(count_upper)