def pairs_sum_to_zero(l):
    # Create a set to store unique elements from the list
    seen = set()
    # Initialize an empty set to store unique pairs
    pairs = set()

    for num in l:
        # Check if the additive inverse (-num) has been seen
        if -num in seen:
            # Add the pair to the pairs set. The use of a tuple and min/max 
            # ensures that each pair is added only once in a consistent order.
            pairs.add((min(num, -num), max(num, -num)))

        # Add the current number to the set of seen elements
        seen.add(num)

    # Convert the set of tuples to a list
    return list(pairs)

# Example usage
print(pairs_sum_to_zero([2, -1, 1, -2, 2]))  # Example output: [(-2, 2), (-1, 1)]
