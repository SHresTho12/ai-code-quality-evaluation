# This is a generated Python file.
def valid_date(date):
    parts = date.split('-')
    if len(parts) != 3:
        return False
    month, day, year = parts
    if len(month) != 2 or len(day) != 2 or len(year) != 4:
        return False
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if year < 1:
        return False
    return True




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
