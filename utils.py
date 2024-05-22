import datetime

def convert_month(month):
    """Convert month name or number to its numerical value."""
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    if isinstance(month, int):
        return month
    elif isinstance(month, str):
        return months.get(month.capitalize(), None)
    return None

def validate_date(day, month, year):
    """Validate the given date."""
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False
