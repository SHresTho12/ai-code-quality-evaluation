def remove_vowels(text):
    # Define the vowels
    vowels = "aeiouAEIOU"
    
    # Use a list comprehension to filter out the vowels and join the remaining characters
    return ''.join(char for char in text if char not in vowels)

# Example usage
print(remove_vowels("Hello World"))  # Output: "Hll Wrld"
