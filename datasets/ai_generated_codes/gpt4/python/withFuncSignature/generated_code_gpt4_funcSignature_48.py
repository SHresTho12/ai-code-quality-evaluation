def is_palindrome(text: str):
    # Remove non-alphanumeric characters and convert to lower case
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Check if the cleaned text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

# Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("Hello"))  # Output: False
