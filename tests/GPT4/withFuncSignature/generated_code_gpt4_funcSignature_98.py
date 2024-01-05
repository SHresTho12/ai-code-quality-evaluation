def count_upper(s):
    """
    Counts the number of uppercase letters in a string.

    :param s: The string to be checked.
    :return: The count of uppercase letters in the string.
    """
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count


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