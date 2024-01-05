def get_odd_collatz(n):
    """
    Generates the Collatz sequence starting from 'n' and includes only the odd numbers.

    :param n: The starting positive integer.
    :return: A list containing the odd numbers in the Collatz sequence.
    """
    # Initialize an empty list to store the odd numbers in the sequence
    odd_collatz_sequence = []

    while n != 1:
        # Check if the current number is odd
        if n % 2 == 1:
            odd_collatz_sequence.append(n)

        # Apply the Collatz rules
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    # Add 1 to the sequence (the last odd number in the Collatz sequence)
    odd_collatz_sequence.append(1)

    return odd_collatz_sequence


def check(get_odd_collatz):
    # Check some simple cases
    assert get_odd_collatz(14) == [1, 5, 7, 11, 13, 17], "Test 1"
    assert get_odd_collatz(5) == [1, 5], "Test 2"
    assert get_odd_collatz(12) == [1, 3, 5], "Test 3"

    # Check the function
    check(get_odd_collatz)