def anti_shuffle(s):
    """
    Sorts the characters of the string in ascending alphabetical order.

    :param s: The input string.
    :return: A string with characters sorted in ascending alphabetical order.
    """
    return ''.join(sorted(s))


def check(anti_shuffle):
    # Check some simple cases
    assert anti_shuffle('Hi') == 'Hi', "Test 1"
    assert anti_shuffle('hello') == 'ehllo', "Test 2"
    assert anti_shuffle('number') == 'bemnru', "Test 3"
    assert anti_shuffle('abcd') == 'abcd', "Test 4"
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor', "Test 5"
    assert anti_shuffle('') == '', "Test 6"
    assert anti_shuffle('Hi. My name is Mister Robot. How are you?') == '.Hi My aemn is Meirst .Rboot How aer ?ouy', "Test 7"

    # Check some edge cases that are easy to work out by hand.

check(anti_shuffle)