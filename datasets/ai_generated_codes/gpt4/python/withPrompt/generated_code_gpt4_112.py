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
