def digit_sum(n):
    """Helper function to calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(abs(n)))

def strange_sort_list(lst):
    """Sorts the list based on the sum of the digits of each number."""
    return sorted(lst, key=digit_sum)

# Example usage
print(strange_sort_list([112, 24, 31]))  # Output might be [31, 24, 112] since 4, 6, 4 are the respective digit sums
