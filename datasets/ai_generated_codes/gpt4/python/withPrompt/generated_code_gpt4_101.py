def words_string(s):
    # Split the string into words using both commas and spaces as separators
    words = re.split(r'[,\s]+', s)
    # Remove any empty strings from the list
    words = [word for word in words if word]
    return words

# Test cases
print(words_string("Hi, my name is John"))  # Output: ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # Output: ["One", "two", "three", "four", "five", "six"]
