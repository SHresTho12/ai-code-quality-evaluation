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
