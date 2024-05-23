import unittest
from utils import validate_date , convert_month
from life_path import calculate_life_path_number, get_lucky_colour, compare_life_path_numbers, sum_digits
from generation import determine_generation

class TestLifePathNumberBlackBox(unittest.TestCase):

    def test_calculate_life_path_number_valid(self):
        self.assertEqual(calculate_life_path_number((13, 11, 1987)), 22)
        self.assertEqual(calculate_life_path_number((22, 11, 2000)), 8)
        self.assertEqual(calculate_life_path_number((1, 1, 1)), 3)
        self.assertEqual(calculate_life_path_number((31, 12, 2999)), 9)
        self.assertEqual(calculate_life_path_number((11, 11, 1911)), 7)
        self.assertEqual(calculate_life_path_number((22, 12, 1933)), 5)

    def test_calculate_life_path_number_invalid(self):
        with self.assertRaises(ValueError):
            calculate_life_path_number((32, 12, 2020))
        with self.assertRaises(ValueError):
            calculate_life_path_number((29, 2, 2021))  # Non-leap year

    def test_get_lucky_colour(self):
        self.assertEqual(get_lucky_colour(1), "Red")
        self.assertEqual(get_lucky_colour(22), "White")
        self.assertEqual(get_lucky_colour(33), "Crimson")
        self.assertEqual(get_lucky_colour(0), "Unknown")
        self.assertEqual(get_lucky_colour(10), "Unknown")

    def test_compare_life_path_numbers(self):
        self.assertTrue(compare_life_path_numbers((15, 5, 1990), (5, 1, 2004)))
        self.assertFalse(compare_life_path_numbers((15, 5, 1990), (22, 11, 2000)))
        with self.assertRaises(ValueError):
            compare_life_path_numbers((32, 12, 2020), (15, 5, 1990))
        with self.assertRaises(ValueError):
            compare_life_path_numbers((15, 5, 1990), (29, 2, 2021))  # Non-leap year


class TestLifePathNumberWhiteBox(unittest.TestCase):

    def test_sum_digits(self):
        # Assuming sum_digits is part of the calculate_life_path_number
        # Here, we simulate the sum_digits function's behavior
        def sum_digits(num):
            if num in {11, 22, 33}:
                return num
            while num not in {11, 22, 33} and num >= 10:
                num = sum(int(digit) for digit in str(num))
            return int(num)

        self.assertEqual(sum_digits(29), 11)
        self.assertEqual(sum_digits(38), 11)
        self.assertEqual(sum_digits(49), 4)
        self.assertEqual(sum_digits(16), 7)
        self.assertEqual(sum_digits(25), 7)

    def test_calculate_life_path_number_step_by_step(self):
        self.assertEqual(calculate_life_path_number((29, 12, 2020)), 9)
        self.assertEqual(calculate_life_path_number((16, 7, 1987)), 3)

    def test_get_lucky_colour_white_box(self):
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

        for number, colour in colours.items():
            self.assertEqual(get_lucky_colour(number), colour)

    def test_compare_life_path_numbers_white_box(self):
        self.assertTrue(compare_life_path_numbers((15, 5, 1990), (15, 5, 1990)))
        self.assertFalse(compare_life_path_numbers((1, 1, 2000), (2, 2, 2000)))
        self.assertFalse(compare_life_path_numbers((8, 8, 1988), (9, 9, 1989)))

    def test_internal_sum_digits_logic(self):
        self.assertEqual(sum_digits(38), 11)
        self.assertEqual(sum_digits(44), 8)
        self.assertEqual(sum_digits(99), 9)
        self.assertEqual(sum_digits(27), 9)
        self.assertEqual(sum_digits(123), 6)

    def test_calculate_life_path_number_specific_paths(self):
        self.assertEqual(calculate_life_path_number((3, 3, 2000)), 8)
        self.assertEqual(calculate_life_path_number((11, 12, 2011)), 9)
        self.assertEqual(calculate_life_path_number((22, 12, 1999)), 8)

    def test_calculate_life_path_number_equivalence_partitioning(self):
        self.assertEqual(calculate_life_path_number((15, 5, 1990)), 3)
        self.assertEqual(calculate_life_path_number((25, 12, 2000)), 3)
        self.assertEqual(calculate_life_path_number((5, 11, 1985)), 3)

    def test_calculate_life_path_number_invalid_equivalence_partitioning(self):
        with self.assertRaises(ValueError):
            calculate_life_path_number((32, 10, 2020))
        with self.assertRaises(ValueError):
            calculate_life_path_number((0, 10, 2020))

    def test_calculate_life_path_number_day_boundaries(self):
        self.assertEqual(calculate_life_path_number((1, 1, 2000)), 4)
        self.assertEqual(calculate_life_path_number((31, 1, 2000)), 7)
        with self.assertRaises(ValueError):
            calculate_life_path_number((0, 1, 2000))
        with self.assertRaises(ValueError):
            calculate_life_path_number((32, 1, 2000))

    def test_calculate_life_path_number_month_boundaries(self):
        self.assertEqual(calculate_life_path_number((15, 1, 2000)), 9)
        self.assertEqual(calculate_life_path_number((15, 12, 2000)), 11)
        with self.assertRaises(ValueError):
            calculate_life_path_number((15, 0, 2000))
        with self.assertRaises(ValueError):
            calculate_life_path_number((15, 13, 2000))


class TestDetermineGenerationBlackBox(unittest.TestCase):

    def test_silent_generation(self):
        self.assertEqual(determine_generation(1901), 'Silent Generation')
        self.assertEqual(determine_generation(1945), 'Silent Generation')

    def test_baby_boomers(self):
        self.assertEqual(determine_generation(1946), 'Baby Boomers')
        self.assertEqual(determine_generation(1964), 'Baby Boomers')

    def test_generation_x(self):
        self.assertEqual(determine_generation(1965), 'Generation X')
        self.assertEqual(determine_generation(1979), 'Generation X')

    def test_millennials(self):
        self.assertEqual(determine_generation(1980), 'Millennials')
        self.assertEqual(determine_generation(1994), 'Millennials')

    def test_generation_z(self):
        self.assertEqual(determine_generation(1995), 'Generation Z')
        self.assertEqual(determine_generation(2009), 'Generation Z')

    def test_generation_alpha(self):
        self.assertEqual(determine_generation(2010), 'Generation Alpha')
        self.assertEqual(determine_generation(2024), 'Generation Alpha')

    def test_unknown_generation(self):
        self.assertEqual(determine_generation(1900), 'Unknown Generation')
        self.assertEqual(determine_generation(2025), 'Unknown Generation')
        self.assertEqual(determine_generation(1800), 'Unknown Generation')
        self.assertEqual(determine_generation(3000), 'Unknown Generation')

class TestDetermineGenerationWhiteBox(unittest.TestCase):

    def test_silent_generation(self):
        for year in range(1901, 1946):
            self.assertEqual(determine_generation(year), 'Silent Generation')

    def test_baby_boomers(self):
        for year in range(1946, 1965):
            self.assertEqual(determine_generation(year), 'Baby Boomers')

    def test_generation_x(self):
        for year in range(1965, 1980):
            self.assertEqual(determine_generation(year), 'Generation X')

    def test_millennials(self):
        for year in range(1980, 1995):
            self.assertEqual(determine_generation(year), 'Millennials')

    def test_generation_z(self):
        for year in range(1995, 2010):
            self.assertEqual(determine_generation(year), 'Generation Z')

    def test_generation_alpha(self):
        for year in range(2010, 2025):
            self.assertEqual(determine_generation(year), 'Generation Alpha')

    def test_unknown_generation(self):
        self.assertEqual(determine_generation(1900), 'Unknown Generation')
        self.assertEqual(determine_generation(2025), 'Unknown Generation')
        self.assertEqual(determine_generation(1800), 'Unknown Generation')
        self.assertEqual(determine_generation(3000), 'Unknown Generation')

    def test_determine_generation_equivalence_partitioning(self):
        self.assertEqual(determine_generation(1930), 'Silent Generation')
        self.assertEqual(determine_generation(1955), 'Baby Boomers')
        self.assertEqual(determine_generation(1970), 'Generation X')
        self.assertEqual(determine_generation(1990), 'Millennials')
        self.assertEqual(determine_generation(2005), 'Generation Z')

    def test_determine_generation_boundary_values(self):
        self.assertEqual(determine_generation(1901), 'Silent Generation')
        self.assertEqual(determine_generation(1945), 'Silent Generation')
        self.assertEqual(determine_generation(1946), 'Baby Boomers')
        self.assertEqual(determine_generation(1964), 'Baby Boomers')
        self.assertEqual(determine_generation(1965), 'Generation X')
        self.assertEqual(determine_generation(1979), 'Generation X')
        self.assertEqual(determine_generation(1980), 'Millennials')
        self.assertEqual(determine_generation(1994), 'Millennials')
        self.assertEqual(determine_generation(1995), 'Generation Z')
        self.assertEqual(determine_generation(2009), 'Generation Z')
        self.assertEqual(determine_generation(2010), 'Generation Alpha')
        self.assertEqual(determine_generation(2024), 'Generation Alpha')


class TestDateUtilsBlackBox(unittest.TestCase):

    def test_convert_month_name_to_number(self):
        self.assertEqual(convert_month("January"), 1)
        self.assertEqual(convert_month("February"), 2)
        self.assertEqual(convert_month("March"), 3)
        self.assertEqual(convert_month("April"), 4)
        self.assertEqual(convert_month("May"), 5)
        self.assertEqual(convert_month("June"), 6)
        self.assertEqual(convert_month("July"), 7)
        self.assertEqual(convert_month("August"), 8)
        self.assertEqual(convert_month("September"), 9)
        self.assertEqual(convert_month("October"), 10)
        self.assertEqual(convert_month("November"), 11)
        self.assertEqual(convert_month("December"), 12)

    def test_convert_month_number_to_number(self):
        self.assertEqual(convert_month(1), 1)
        self.assertEqual(convert_month(12), 12)

    def test_convert_month_invalid(self):
        self.assertIsNone(convert_month("InvalidMonth"))
        self.assertIsNone(convert_month(None))

    def test_validate_date_valid(self):
        self.assertTrue(validate_date(15, 5, 1990))
        self.assertTrue(validate_date(29, 2, 2020))  # Leap year
        self.assertTrue(validate_date(31, 12, 1999))

    def test_validate_date_invalid(self):
        self.assertFalse(validate_date(32, 1, 2020))
        self.assertFalse(validate_date(29, 2, 2019))  # Not a leap year
        self.assertFalse(validate_date(31, 4, 2020))  # April has 30 days
        self.assertFalse(validate_date(0, 1, 2020))
        self.assertFalse(validate_date(1, 13, 2020))


class TestDateUtilsWhiteBox(unittest.TestCase):

    def test_convert_month_all_cases(self):
        months = {
            "January": 1, "February": 2, "March": 3, "April": 4,
            "May": 5, "June": 6, "July": 7, "August": 8,
            "September": 9, "October": 10, "November": 11, "December": 12
        }

        for month_name, month_num in months.items():
            self.assertEqual(convert_month(month_name), month_num)
            self.assertEqual(convert_month(month_name.lower()), month_num)
            self.assertEqual(convert_month(month_name.upper()), month_num)

    def test_convert_month_invalid_cases(self):
        self.assertIsNone(convert_month("InvalidMonth"))
        self.assertIsNone(convert_month(None))

    def test_convert_month_numeric(self):
        for i in range(1, 13):
            self.assertEqual(convert_month(i), i)

    def test_validate_date_valid(self):
        self.assertTrue(validate_date(1, 1, 2000))
        self.assertTrue(validate_date(31, 1, 2000))
        self.assertTrue(validate_date(29, 2, 2000))  # Leap year
        self.assertTrue(validate_date(30, 4, 2000))
        self.assertTrue(validate_date(31, 12, 2000))

    def test_validate_date_invalid(self):
        self.assertFalse(validate_date(0, 1, 2000))
        self.assertFalse(validate_date(32, 1, 2000))
        self.assertFalse(validate_date(29, 2, 2001))  # Not a leap year
        self.assertFalse(validate_date(31, 4, 2000))  # April has 30 days
        self.assertFalse(validate_date(1, 13, 2000))

    def test_validate_date_equivalence_partitioning(self):
        self.assertTrue(validate_date(10, 10, 2020))
        self.assertTrue(validate_date(1, 1, 2021))
        self.assertTrue(validate_date(28, 2, 2021))

    def test_validate_date_invalid_equivalence_partitioning(self):
        self.assertFalse(validate_date(32, 10, 2020))
        self.assertFalse(validate_date(0, 10, 2020))
        self.assertFalse(validate_date(31, 11, 2020))

    def test_validate_date_day_boundaries(self):
        self.assertTrue(validate_date(1, 1, 2020))
        self.assertTrue(validate_date(31, 1, 2020))
        self.assertFalse(validate_date(0, 1, 2020))
        self.assertFalse(validate_date(32, 1, 2020))

    def test_validate_date_month_boundaries(self):
        self.assertTrue(validate_date(15, 1, 2020))
        self.assertTrue(validate_date(15, 12, 2020))
        self.assertFalse(validate_date(15, 0, 2020))
        self.assertFalse(validate_date(15, 13, 2020))


if __name__ == '__main__':
    unittest.main()
