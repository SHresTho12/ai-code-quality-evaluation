def is_bored(S):
    """
    Count the number of boredoms (sentences starting with "I") in the input string.
    """
    # Split the string into sentences based on '.', '?' or '!'
    sentences = S.split('.') + S.split('?') + S.split('!')

    # Count the number of boredoms (sentences starting with "I")
    boredom_count = 0
    for sentence in sentences:
        words = sentence.strip().split()
        if len(words) > 0 and words[0].lower() == 'i':
            boredom_count += 1

    return boredom_count

# Test cases
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
