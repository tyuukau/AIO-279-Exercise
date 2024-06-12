import unittest
from w02.ex_01_max_in_sliding_window import max_in_sliding_window


class TestMaxInSlidingWindow(unittest.TestCase):
    def test_max_in_sliding_window(self):
        num_list = [1, -1, -1, -3, 5, 3, 6, 7]
        k = 3
        window_generator = max_in_sliding_window(num_list, k)
        self.assertEqual(next(window_generator), 1)
        self.assertIsNone(next(window_generator))
        self.assertEqual(next(window_generator), 5)
        self.assertEqual(next(window_generator), 5)
        self.assertEqual(next(window_generator), 6)
        self.assertEqual(next(window_generator), 7)

        num_list = [3, -1, -1, -1, -44, 5, 10, 12, 33, 1]
        k = 3
        window_generator = max_in_sliding_window(num_list, k)
        self.assertEqual(next(window_generator), 3)
        self.assertIsNone(next(window_generator))
        self.assertIsNone(next(window_generator))
        self.assertEqual(next(window_generator), 5)
        self.assertEqual(next(window_generator), 10)
        self.assertEqual(next(window_generator), 12)
        self.assertEqual(next(window_generator), 33)
        self.assertEqual(next(window_generator), 33)

        num_list = [1, 2, 3, 4, 5]
        k = 1
        window_generator = max_in_sliding_window(num_list, k)
        self.assertEqual(next(window_generator), 1)
        self.assertEqual(next(window_generator), 2)
        self.assertEqual(next(window_generator), 3)
        self.assertEqual(next(window_generator), 4)
        self.assertEqual(next(window_generator), 5)

        num_list = [5, 4, 3, 2, 1]
        k = 5
        window_generator = max_in_sliding_window(num_list, k)
        self.assertEqual(next(window_generator), 5)

        num_list = [1, 2, 3, 4, 5]
        k = 2
        window_generator = max_in_sliding_window(num_list, k)
        self.assertEqual(next(window_generator), 2)
        self.assertEqual(next(window_generator), 3)
        self.assertEqual(next(window_generator), 4)
        self.assertEqual(next(window_generator), 5)

        num_list = [1, 2, 3, 4, 5]
        k = 4
        window_generator = max_in_sliding_window(num_list, k)
        self.assertEqual(next(window_generator), 4)
        self.assertEqual(next(window_generator), 5)

        num_list = [1, 2, 3, 4, 5]
        k = 5
        window_generator = max_in_sliding_window(num_list, k)
        self.assertEqual(next(window_generator), 5)

        num_list = [1, 2, 3, 4, 5]
        k = 2
        window_generator = max_in_sliding_window(num_list, k)
        self.assertEqual(next(window_generator), 2)
        self.assertEqual(next(window_generator), 3)
        self.assertEqual(next(window_generator), 4)
        self.assertEqual(next(window_generator), 5)

    def test_raises_value_error(self):
        num_list = []
        k = 3
        window_generator = max_in_sliding_window(num_list, k)
        with self.assertRaises(ValueError):
            next(window_generator)

        num_list = [1, 2, 3, 4, 5]
        k = 6
        window_generator = max_in_sliding_window(num_list, k)
        with self.assertRaises(ValueError):
            next(window_generator)

        num_list = [1, 2, 3, 4, 5]
        k = 0
        window_generator = max_in_sliding_window(num_list, k)
        with self.assertRaises(ValueError):
            next(window_generator)

        num_list = [1, 2, 3, 4, 5]
        k = -1
        window_generator = max_in_sliding_window(num_list, k)
        with self.assertRaises(ValueError):
            next(window_generator)


if __name__ == "__main__":
    unittest.main()
