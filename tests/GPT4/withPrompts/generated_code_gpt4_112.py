def reverse_delete(s, c):
    # Remove characters in s that are equal to any character in c
    result = ''.join([char for char in s if char not in c])

    # Check if the result string is a palindrome
    is_palindrome = result == result[::-1]

    return (result, is_palindrome)

# Test cases
print(reverse_delete("abcde", "ae"))       # Output: ('bcd', False)
print(reverse_delete("abcdef", "b"))       # Output: ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))   # Output: ('cdedc', True)
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