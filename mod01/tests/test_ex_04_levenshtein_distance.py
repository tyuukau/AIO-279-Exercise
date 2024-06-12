import unittest
from w02.ex_04_levenshtein_distance import levenshtein_distance


class LevenshteinDistanceTests(unittest.TestCase):
    def test_same_strings(self):
        s1 = "hello"
        s2 = "hello"
        self.assertEqual(levenshtein_distance(s1, s2), 0)

    def test_empty_strings(self):
        s1 = ""
        s2 = ""
        self.assertEqual(levenshtein_distance(s1, s2), 0)

    def test_different_lengths(self):
        s1 = "kitten"
        s2 = "sitting"
        self.assertEqual(levenshtein_distance(s1, s2), 3)

    def test_case_sensitive(self):
        s1 = "GitHub"
        s2 = "github"
        self.assertEqual(levenshtein_distance(s1, s2), 2)


if __name__ == "__main__":
    unittest.main()
