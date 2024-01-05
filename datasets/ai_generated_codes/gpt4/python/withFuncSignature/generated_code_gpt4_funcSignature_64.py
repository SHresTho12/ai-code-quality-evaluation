FIX = """
Add more test cases to ensure the function handles various scenarios correctly:
- Test with a string containing all vowels.
- Test with a string containing no vowels.
- Test with a string that includes both uppercase and lowercase letters.
- Test with special characters and numbers to ensure they're not counted as vowels.
- Test with an empty string.
"""

def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    :param s: A string in which to count vowels.
    :return: The number of vowels in the string.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)
