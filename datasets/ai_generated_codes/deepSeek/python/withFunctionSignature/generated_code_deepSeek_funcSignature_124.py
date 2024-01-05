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