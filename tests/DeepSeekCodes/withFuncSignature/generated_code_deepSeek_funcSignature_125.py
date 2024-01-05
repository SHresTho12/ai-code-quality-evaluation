
def split_words(txt):
    return txt.split()


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
