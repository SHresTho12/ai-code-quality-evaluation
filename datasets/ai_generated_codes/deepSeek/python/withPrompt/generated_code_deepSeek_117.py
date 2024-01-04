def select_words(s, n):
    vowels = 'aeiouAEIOU'
    words = s.split()
    result = []
    for word in words:
        count = sum(1 for c in word if c not in vowels)
        if count == n:
            result.append(word)
    return result