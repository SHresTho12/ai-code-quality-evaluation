
def exchange(lst1, lst2):
  """
  This function exchanges the elements of two lists at the same index.

  Args:
      lst1: The first list.
      lst2: The second list.

  Returns:
      Two new lists with the elements exchanged.
  """

  # Check if the lists have the same length
  if len(lst1) != len(lst2):
    raise ValueError("Lists must be the same length")

  # Create new lists to store the exchanged elements
  new_lst1 = []
  new_lst2 = []

  # Loop through the lists and exchange elements at each index
  for i in range(len(lst1)):
    new_lst1.append(lst2[i])
    new_lst2.append(lst1[i])

  return new_lst1, new_lst2
