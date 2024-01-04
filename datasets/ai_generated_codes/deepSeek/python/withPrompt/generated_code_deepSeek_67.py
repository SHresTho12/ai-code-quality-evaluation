def fruit_distribution(s,n):
    # Split the string into a list of words
    words = s.split()
    # Extract the number of apples and oranges
    apples = int(words[0])
    oranges = int(words[2])
    # Calculate the number of mangoes
    mangoes = n - apples - oranges
    return mangoes