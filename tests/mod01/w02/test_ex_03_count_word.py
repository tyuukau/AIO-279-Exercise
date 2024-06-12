import unittest
import os

from mod01.w02.ex_03_count_word import count_word_in_file


class TestCountWordInFile(unittest.TestCase):
    def test_count_word_in_file(self):
        # Test case 1: Empty file
        file_path = os.path.join(os.path.dirname(__file__), "data", "empty_file.txt")
        expected_result = {}
        self.assertEqual(count_word_in_file(file_path), expected_result)

        # Test case 2: File with one word
        file_path = os.path.join(os.path.dirname(__file__), "data", "one_word_file.txt")
        expected_result = {"hello": 1}
        self.assertEqual(count_word_in_file(file_path), expected_result)

        # Test case 3: File with multiple words
        file_path = os.path.join(os.path.dirname(__file__), "data", "multiple_words_file.txt")
        expected_result = {"hello": 2, "world": 1, "python": 3}
        self.assertEqual(count_word_in_file(file_path), expected_result)

        # Test case 4: Non-existent file
        file_path = os.path.join(os.path.dirname(__file__), "data", "non_existent_file.txt")
        expected_result = {}
        self.assertEqual(count_word_in_file(file_path), expected_result)


if __name__ == "__main__":
    unittest.main()
