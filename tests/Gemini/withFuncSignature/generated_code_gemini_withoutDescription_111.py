
def histogram(test):
  """
  Creates a histogram dictionary for the given list of values.

  Args:
    test: A list of values for which to create a histogram.

  Returns:
    A dictionary representing the histogram, where keys are the unique values
    in the list and values are the counts of those values.
  """

  histogram = {}
  for value in test:
    if value in histogram:
      histogram[value] += 1
    else:
      histogram[value] = 1

  return histogram


def check(histogram):
    # Check some simple cases
    assert histogram('a b b a') == {'a': 2, 'b': 2}, "Test 1"
    assert histogram('a b c a b') == {'a': 2, 'b': 2, 'c': 1}, "Test 2"
    assert histogram('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, "Test 3"
    assert histogram('r t g') == {'r': 1, 't': 1, 'g': 1}, "Test 4"
    assert histogram('b b b b a') == {'b': 4, 'a': 1}, "Test 5"
    
    # Check some edge cases that are easy to work out by hand.
    assert histogram('') == {}, "Test 6"
    assert histogram('a') == {'a': 1}, "Test 7"

check(histogram)
