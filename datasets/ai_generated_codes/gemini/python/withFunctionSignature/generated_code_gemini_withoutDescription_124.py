
import datetime

def valid_date(date):
  """
  Checks if a given string represents a valid date.

  Args:
      date: A string representing a date in the format "YYYY-MM-DD".

  Returns:
      True if the date is valid, False otherwise.
  """
  try:
    # Attempt to parse the date string using the `datetime` module.
    datetime.datetime.strptime(date, "%Y-%m-%d")
    return True
  except ValueError:
    # If parsing fails, the date is invalid.
    return False

# Example usage
date1 = "2023-10-27"
date2 = "2024-02-30"

print(f"{date1} is valid: {valid_date(date1)}")
print(f"{date2} is valid: {valid_date(date2)}")
