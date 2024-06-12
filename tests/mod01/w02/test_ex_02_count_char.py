import unittest
from mod01.w02.ex_02_count_char import count_char


class TestCountChar(unittest.TestCase):
    def test_count_char(self):
        # Test case 1: Empty string
        self.assertEqual(count_char(""), {})

        # Test case 2: String with repeated characters
        self.assertEqual(count_char("Hello"), {"H": 1, "e": 1, "l": 2, "o": 1})

        # Test case 3: String with special characters
        self.assertEqual(
            count_char("!@#$%^&*()"),
            {"!": 1, "@": 1, "#": 1, "$": 1, "%": 1, "^": 1, "&": 1, "*": 1, "(": 1, ")": 1},
        )

        # Test case 4: String with numbers
        self.assertEqual(
            count_char("1234567890"),
            {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 1, "9": 1, "0": 1},
        )

        # Test case 5: String with repeated and non-repeated characters
        self.assertEqual(count_char("aabbcde"), {"a": 2, "b": 2, "c": 1, "d": 1, "e": 1})


if __name__ == "__main__":
    unittest.main()
