def max_element(l: list):
    # Check if the list is empty
    if not l:
        return "The list is empty."

    # Return the maximum element
    return max(l)
METADATA = {} 
def check(max_element): 
  assert max_element([1, 2, 3]) == 3 
  assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124 
  
check(max_element)