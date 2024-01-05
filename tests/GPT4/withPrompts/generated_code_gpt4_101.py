def words_string(s):
    # Split the string into words using both commas and spaces as separators
    words = re.split(r'[,\s]+', s)
    # Remove any empty strings from the list
    words = [word for word in words if word]
    return words

# Test cases
print(words_string("Hi, my name is John"))  # Output: ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # Output: ["One", "two", "three", "four", "five", "six"]
def check(words_string):
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"], "Test 1"
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"], "Test 2"
    assert words_string("Hi, my name") == ["Hi", "my", "name"], "Test 3"
    assert words_string("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"], "Test 4"

# Check some edge cases that are easy to work out by hand.
assert words_string("") == [], "Edge Test 1"
assert words_string("ahmed , gamal") == ["ahmed", "gamal"], "Edge Test 2"

check(words_string)