
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



def is_leap_year(year):
    """Checks if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0



def check(valid_date):
    # Check some simple cases
    assert valid_date('03-11-2000') == True, "Test 1"
    assert valid_date('15-01-2012') == False, "Test 2"
    assert valid_date('04-0-2040') == False, "Test 3"
    assert valid_date('06-04-2020') == True, "Test 4"
    assert valid_date('01-01-2007') == True, "Test 5"
    assert valid_date('03-32-2011') == False, "Test 6"
    assert valid_date('') == False, "Test 7"
    assert valid_date('04-31-3000') == False, "Test 8"
    assert valid_date('06-06-2005') == True, "Test 9"
    assert valid_date('21-31-2000') == False, "Test 10"
    assert valid_date('04-12-2003') == True, "Test 11"
    assert valid_date('04122003') == False, "Test 12"
    assert valid_date('20030412') == False, "Test 13"
    assert valid_date('2003-04') == False, "Test 14"
    assert valid_date('2003-04-12') == False, "Test 15"
    assert valid_date('04-2003') == False, "Test 16"

    # Check the function
    check(valid_date)
