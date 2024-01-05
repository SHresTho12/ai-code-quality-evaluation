def split_words(txt):
    # Check if the text contains whitespaces
    if ' ' in txt:
        # Split on whitespaces and return the list of words
        return txt.split()
    elif ',' in txt:
        # Split on commas and return the list of words
        return txt.split(',')
    else:
        # Count the number of lowercase letters with odd order in the alphabet
        # Calculate the ASCII value of 'a' to determine the offset
        offset = ord('a')
        count = sum(1 for char in txt if char.islower() and (ord(char) - offset) % 2 == 1)
        return count

# Test cases
print(split_words("Hello world!"))     # ["Hello", "world!"]
print(split_words("Hello,world!"))     # ["Hello", "world!"]
print(split_words("abcdef"))           # 3
def check(split_words):
    # Check some simple cases
    assert split_words("Hello world!") == ["Hello", "world!"], "Test 1"
    assert split_words("Hello,world!") == ["Hello", "world!"], "Test 2"
    assert split_words("Hello world,!") == ["Hello", "world,!"], "Test 3"
    assert split_words("Hello,Hello,world !") == ["Hello,Hello,world", "!"], "Test 4"
    
    # Check some cases with unique words
    assert split_words("abcdef") == 3, "Test 5"
    assert split_words("aaabb") == 2, "Test 6"
    assert split_words("aaaBb") == 1, "Test 7"
    
    # Check an empty string
    assert split_words("") == 0, "Test 8"

    # Check the function
    check(split_words)
