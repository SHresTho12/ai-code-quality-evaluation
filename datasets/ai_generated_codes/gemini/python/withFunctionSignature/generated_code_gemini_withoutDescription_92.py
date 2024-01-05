
def any_int(x, y, z):
  """Returns True if any of the arguments are integers, False otherwise."""
  return any(isinstance(arg, int) for arg in (x, y, z))
