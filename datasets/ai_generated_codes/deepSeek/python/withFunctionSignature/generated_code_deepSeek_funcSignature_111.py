# This is a generated Python file.
def histogram(test):
    hist = {}
    for char in test:
        if char in hist:
            hist[char] += 1
        else:
            hist[char] = 1
    return hist