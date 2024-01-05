def anti_shuffle(s):
    """
    Takes a string and returns an ordered version of it.
    Ordered version of a string has words with characters arranged in ascending order.
    """
    # Split the input string into words
    words = s.split()

    # Initialize a list to store the ordered words
    ordered_words = []

    # Iterate through the words
    for word in words:
        # Sort the characters in the word in ascending order
        ordered_word = ''.join(sorted(word))

        # Add the ordered word to the list
        ordered_words.append(ordered_word)

    # Reconstruct the ordered string with the same word order and spaces
    ordered_string = ' '.join(ordered_words)

    return ordered_string
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