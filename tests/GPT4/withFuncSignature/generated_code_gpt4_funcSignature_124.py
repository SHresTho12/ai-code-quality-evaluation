def valid_date(date):
    """
    Validates if a date string is in the format "YYYY-MM-DD" and represents a valid date.

    :param date: The input date string to validate.
    :return: True if the date is valid, False otherwise.
    """
    try:
        # Split the date string into year, month, and day components
        year, month, day = date.split('-')

        # Convert components to integers
        year = int(year)
        month = int(month)
        day = int(day)

        # Check if the year, month, and day are within valid ranges
        if (
            1 <= month <= 12 and
            1 <= day <= 31 and
            1900 <= year <= 2100  # Change the range as needed
        ):
            return True
        else:
            return False

    except (ValueError, IndexError):
        # Handle exceptions for invalid format or missing components
        return False


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