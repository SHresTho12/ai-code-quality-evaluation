def check_dict_case(d):
    """
    Checks if all string keys in the dictionary are in lowercase.

    :param d: The dictionary to check.
    :return: True if all string keys are in lowercase, False otherwise.
    """
    for key in d.keys():
        if isinstance(key, str) and not key.islower():
            return False
    return True
