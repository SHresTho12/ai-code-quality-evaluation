
def reverse_delete(s, c):
    """
    Deletes characters in s that are in c, then checks if the remaining string is a palindrome.

    Args:
        s: The original string.
        c: The string containing characters to be deleted.

    Returns:
        A tuple containing:
            - The modified string after character deletions.
            - True if the modified string is a palindrome, False otherwise.
    """

    result = ""
    for char in s:
        if char not in c:
            result += char

    return result, result == result[::-1]  # Check for palindrome

def check(reverse_delete):
    # Check some simple cases
    assert reverse_delete("abcde", "ae") == ('bcd', False), "Test 1"
    assert reverse_delete("abcdef", "b") == ('acdef', False), "Test 2"
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True), "Test 3"
    assert reverse_delete("dwik", "w") == ('dik', False), "Test 4"
    assert reverse_delete("a", "a") == ('', True), "Test 5"
    assert reverse_delete("abcdedcba", "") == ('abcdedcba', True), "Test 6"
    assert reverse_delete("abcdedcba", "v") == ('abcdedcba', True), "Test 7"
    assert reverse_delete("vabba", "v") == ('abba', True), "Test 8"
    assert reverse_delete("mamma", "mia") == ("", True), "Test 9"

check(reverse_delete)
