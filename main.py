import life_path
import generation
import utils

def get_user_birthdate():
    """Get and validate user input for the birthdate."""
    try:
        day = int(input("Enter the day (DD): "))
        month_input = input("Enter the month (MM or Month name): ")
        year = int(input("Enter the year (YYYY): "))

        # Convert month names to numbers if necessary
        month = utils.convert_month(month_input)
        if month is None:
            try:
                month = int(month_input)
            except ValueError:
                print(f"Invalid month: {month_input}")
                return None

        birthdate = (day, month, year)
        if not utils.validate_date(*birthdate):
            print("Invalid date:", birthdate)
            return None

        return birthdate
    except ValueError:
        print("Invalid input. Please enter numeric values for day and year.")
        return None

def display_menu():
    """Display the menu options."""
    print("====================================")
    print("          MENU                      ")
    print("====================================")
    print("1. Calculate Life Path Number and Lucky Colour for two birthdays")
    print("2. Calculate Life Path Number and Lucky Colour for one birthday")
    print("3. Determine Generation")
    print("4. Exit")
    print("====================================")


def analyze_single_birthdate():
    """Analyze a single birthdate."""
    print("Calculate Life Path Number and Lucky Colour")
    birthdate = get_user_birthdate()
    if not birthdate:
        return

    # Calculate Life Path Number
    lp = life_path.calculate_life_path_number(birthdate)

    # Output Life Path Number and Lucky Colour
    print("\n")
    print(f"Life Path Number for {birthdate}: {lp}")
    print(f"Lucky Colour for {birthdate}: {life_path.get_lucky_colour(lp)}")
    print("\n")


def main():
    """Main function to execute the numerology analysis."""
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print("Calculate Life Path Number and Lucky Colour for two birthdays")
            birthdate1 = get_user_birthdate()
            if not birthdate1:
                continue

            birthdate2 = get_user_birthdate()
            if not birthdate2:
                continue

            # Calculate Life Path Numbers
            lp1 = life_path.calculate_life_path_number(birthdate1)
            lp2 = life_path.calculate_life_path_number(birthdate2)

            # Output Life Path Numbers and Lucky Colours
            print("\n")
            print(f"Life Path Number for {birthdate1}: {lp1}")
            print(f"Lucky Colour for {birthdate1}: {life_path.get_lucky_colour(lp1)}")
            print(f"Life Path Number for {birthdate2}: {lp2}")
            print(f"Lucky Colour for {birthdate2}: {life_path.get_lucky_colour(lp2)}")

            # Check if Life Path Numbers are the same
            same_lp = life_path.compare_life_path_numbers(birthdate1, birthdate2)
            print(f"Do both birthdates have the same Life Path Number? {same_lp}")
            print("\n")

        elif choice == '2':
            analyze_single_birthdate()

        elif choice == '3':
            print("Determine Generation")
            birthdate = get_user_birthdate()
            if not birthdate:
                continue

            generation_name = generation.determine_generation(birthdate[2])
            print(f"Generation for {birthdate}: {generation_name}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

