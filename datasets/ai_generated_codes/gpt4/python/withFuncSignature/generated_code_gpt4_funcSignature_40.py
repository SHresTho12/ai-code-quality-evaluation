def triples_sum_to_zero(l: list):
    # Sort the list to make it easier to skip duplicates and use two-pointer technique
    l.sort()
    result = []

    for i in range(len(l) - 2):
        # Skip duplicate elements
        if i > 0 and l[i] == l[i-1]:
            continue

        # Use two pointers to find pairs that sum up to the negative of l[i]
        left, right = i + 1, len(l) - 1
        while left < right:
            total = l[i] + l[left] + l[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # Found a triplet that sums up to zero
                result.append([l[i], l[left], l[right]])

                # Skip duplicates
                while left < right and l[left] == l[left + 1]:
                    left += 1
                while left < right and l[right] == l[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result

# Example usage
print(triples_sum_to_zero([-1, 0, 1, 2, -1, -4]))  # Example output: [[-1, -1, 2], [-1, 0, 1]]
