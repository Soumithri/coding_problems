import unittest
try:
    from coding_problems.src.algorithms.highest_product_of_3 import solution
except ImportError as e:
    from coding_problems.src.algorithms.answers.highest_product_of_3 import \
        solution


class Test_Highest_Product_Of_3(unittest.TestCase):

    def test_short_list(self):
        actual = solution([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = solution([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = solution([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = solution([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = solution([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            solution([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            solution([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            solution([1, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
