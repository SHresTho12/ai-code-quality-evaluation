def select_words(s, n):
    def count_consonants(word):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for letter in word if letter in consonants)

    words = s.split()
    selected_words = [word for word in words if count_consonants(word) == n]

    return selected_words

# Test cases
print(select_words("Mary had a little lamb", 4))  # Output: ["little"]
print(select_words("Mary had a little lamb", 3))  # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))  # Output: []
print(select_words("Hello world", 4))  # Output: ["world"]
print(select_words("Uncle sam", 3))  # Output: ["Uncle"]
