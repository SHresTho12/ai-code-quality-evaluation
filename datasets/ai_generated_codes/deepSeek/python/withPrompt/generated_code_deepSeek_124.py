def valid_date(date):
    if not date:
        return False

    parts = date.split('-')
    if len(parts) != 3:
        return False

    month, day, year = parts
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    month, day, year = int(month), int(day), int(year)
    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2:
        if day > 29:
            return False
        if year % 4 != 0 and day > 28:
            return False

    return True