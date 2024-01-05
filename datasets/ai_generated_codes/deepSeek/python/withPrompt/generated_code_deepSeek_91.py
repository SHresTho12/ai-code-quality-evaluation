def is_bored(S):
    sentences = [sentence.strip() for sentence in S.replace('!', '.').replace('?', '.').split('.') if sentence]
    return sum(1 for sentence in sentences if sentence.startswith('I'))