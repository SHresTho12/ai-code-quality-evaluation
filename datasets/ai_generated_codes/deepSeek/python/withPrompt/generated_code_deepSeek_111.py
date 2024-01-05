def histogram(test):
    from collections import Counter
    count = Counter(test.split())
    max_count = max(count.values(), default=0)
    return {k: v for k, v in count.items() if v == max_count}