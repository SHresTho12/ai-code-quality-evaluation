def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False

    # Split the date string into components (month, day, year) using '-'
    date_components = date.split('-')

    # Check if there are exactly 3 components
    if len(date_components) != 3:
        return False

    # Extract month, day, and year as integers
    try:
        month = int(date_components[0])
        day = int(date_components[1])
        year = int(date_components[2])
    except ValueError:
        return False

    # Check if the month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # Define a dictionary to map months to their maximum days
    max_days_in_month = {
        1: 31,  # January
        2: 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,  # February (leap year check)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31,  # December
    }

    # Check if the day is within the valid range for the given month
    if day < 1 or day > max_days_in_month[month]:
        return False

    # Check if the year is a positive integer
    if year < 1:
        return False

    # If all checks passed, the date is valid
    return True

# Test cases
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
