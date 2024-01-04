
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
