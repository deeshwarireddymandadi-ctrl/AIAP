import unittest
from datetime import datetime

def convert_date_format(date_str: str) -> str:
    """
    Convert a date string from 'YYYY-MM-DD' to 'DD-MM-YYYY'.
    Raises:
      TypeError: if date_str is not a str
      ValueError: if date_str is not a valid date in YYYY-MM-DD format
    """
    if not isinstance(date_str, str):
        raise TypeError("date_str must be a string")
    s = date_str.strip()
    try:
        dt = datetime.strptime(s, "%Y-%m-%d")
    except Exception:
        raise ValueError("date_str must be in 'YYYY-MM-DD' and represent a valid date")
    return dt.strftime("%d-%m-%Y")

class ConvertDateFormatTests(unittest.TestCase):
    def test_basic_conversion(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")

    def test_leading_zeros(self):
        self.assertEqual(convert_date_format("2001-01-02"), "02-01-2001")

    def test_whitespace_is_ignored(self):
        self.assertEqual(convert_date_format(" 2023-10-15 "), "15-10-2023")

    def test_valid_leap_day(self):
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")

    def test_invalid_leap_day_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("2019-02-29")

    def test_wrong_separator_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/10/15")

    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_none_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            convert_date_format(None)

    def test_invalid_month_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-01")

    def test_invalid_day_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-04-31")

    def test_extra_time_component_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-15T00:00:00")

    def test_non_numeric_parts_raises(self):
        with self.assertRaises(ValueError):
            convert_date_format("20xx-yy-zz")

    def test_return_type_is_string(self):
        out = convert_date_format("1999-12-31")
        self.assertIsInstance(out, str)
        self.assertEqual(out, "31-12-1999")

if __name__ == "__main__":
    unittest.main(verbosity=2)