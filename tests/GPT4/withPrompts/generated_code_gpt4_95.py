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
def check(check_dict_case):
    # Check some simple cases
    assert check_dict_case({"p":"pineapple", "b":"banana"}) == True, "First test error: " + str(check_dict_case({"p":"pineapple", "b":"banana"}))
    assert check_dict_case({"p":"pineapple", "A":"banana", "B":"banana"}) == False, "Second test error: " + str(check_dict_case({"p":"pineapple", "A":"banana", "B":"banana"}))
    assert check_dict_case({"p":"pineapple", 5:"banana", "a":"apple"}) == False, "Third test error: " + str(check_dict_case({"p":"pineapple", 5:"banana", "a":"apple"}))
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False, "Fourth test error: " + str(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
    assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True, "Fifth test error: " + str(check_dict_case({"STATE":"NC", "ZIP":"12345" }))
    assert check_dict_case({"fruit":"Orange", "taste":"Sweet" }) == True, "Fourth test error: " + str(check_dict_case({"fruit":"Orange", "taste":"Sweet" }))

    # Check some edge cases that are easy to work out by hand.
    assert check_dict_case({}) == False, "1st edge test error: " + str(check_dict_case({}))

check(check_dict_case)