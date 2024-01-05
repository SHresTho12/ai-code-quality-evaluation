def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        # There is only one n-digit positive integer that starts or ends with 1, which is 1 itself.
        return 1
    else:
        # For numbers with more than 1 digit, there are 9 choices for the first digit (1-9)
        # and 10 choices for the last digit (0-9, including 1).
        # For the digits in between, there are 10 choices for each digit (0-9).
        # So, the total count is 9 * 10^(n-2) * 2, where 2 accounts for both starting and ending with 1.
        return 9 * 10**(n-2) * 2
def check(starts_one_ends):
    # Check some simple cases
    assert starts_one_ends(1) == 1, "Test 1"
    assert starts_one_ends(2) == 18, "Test 2"
    assert starts_one_ends(3) == 180, "Test 3"
    assert starts_one_ends(4) == 1800, "Test 4"
    assert starts_one_ends(5) == 18000, "Test 5"

check(starts_one_ends)