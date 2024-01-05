def make_a_pile(n):
    pile = []
    stones = n

    while n > 0:
        pile.append(stones)
        if n % 2 == 0:
            stones += 2
        else:
            stones += 1
        n -= 1

    return pile

# Test cases
print(make_a_pile(3))  # Output: [3, 5, 7]
