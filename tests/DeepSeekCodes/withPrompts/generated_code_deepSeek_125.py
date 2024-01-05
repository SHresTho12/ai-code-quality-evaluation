def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 == 1)
    

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
