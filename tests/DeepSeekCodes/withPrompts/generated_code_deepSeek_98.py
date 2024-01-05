def count_upper(s):
    vowels = 'AEIOU'
    return sum(1 for i in range(len(s)) if i % 2 == 0 and s[i] in vowels)



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