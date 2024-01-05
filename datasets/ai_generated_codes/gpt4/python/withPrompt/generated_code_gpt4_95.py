def check_dict_case(d):
    if not d:
        return False  # Return False for empty dictionary
    
    lowercase_keys = all(key.islower() for key in d.keys())
    uppercase_keys = all(key.isupper() for key in d.keys())
    
    return lowercase_keys or uppercase_keys

# Test cases
print(check_dict_case({"a":"apple", "b":"banana"}))               # Output: True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # Output: False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))     # Output: False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # Output: False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))             # Output: True
