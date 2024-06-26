import re


def words_string(s):
    return re.findall(r'\b\w+\b', s)


def check(words_string):
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"], "Test 1"
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"], "Test 2"
    assert words_string("Hi, my name") == ["Hi", "my", "name"], "Test 3"
    assert words_string("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"], "Test 4"

# Check some edge cases that are easy to work out by hand.
assert words_string("") == [], "Edge Test 1"
assert words_string("ahmed , gamal") == ["ahmed", "gamal"], "Edge Test 2"

check(words_string)