
def check_dict_case(dict):
  """
  This function checks if all keys in a dictionary have a consistent case (either all lowercase or all uppercase).

  Args:
    dict: The dictionary to check.

  Returns:
    True if all keys have a consistent case, False otherwise.
  """

  lower_keys = all(key.islower() for key in dict.keys())
  upper_keys = all(key.isupper() for key in dict.keys())
  return lower_keys or upper_keys
