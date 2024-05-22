from utils import validate_date

def sum_digits(num):
    if num in {11, 22, 33}:
        return num
    while num not in {11, 22, 33} and num >= 10:
        num = sum(int(digit) for digit in str(num))
    return int(num)

def calculate_life_path_number(birthdate):
    day, month, year = birthdate
    if not validate_date(day, month, year):
        raise ValueError("Invalid date")

    # Step 1: Reduce day, month, and year separately
    day_sum = sum_digits(day)
    month_sum = sum_digits(month)
    year_sum = sum_digits(year)

    # Step 2: Sum the results
    total_sum = day_sum + month_sum + year_sum

    # Step 3: Reduce to single digit unless it's a master number
    while total_sum not in {11, 22, 33} and total_sum >= 10:
        total_sum = sum_digits(total_sum)

    return total_sum


def get_lucky_colour(life_path_number):
    """Get the lucky colour based on the life path number."""
    colours = {
        1: "Red",
        2: "Orange",
        3: "Yellow",
        4: "Green",
        5: "Sky Blue",
        6: "Indigo",
        7: "Violet",
        8: "Magenta",
        9: "Gold",
        11: "Silver",
        22: "White",
        33: "Crimson"
    }
    return colours.get(life_path_number, "Unknown")

def compare_life_path_numbers(birthdate1, birthdate2):
    """Compare the life path numbers of two birthdates."""
    lp1 = calculate_life_path_number(birthdate1)
    lp2 = calculate_life_path_number(birthdate2)
    return lp1 == lp2

