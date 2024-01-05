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
