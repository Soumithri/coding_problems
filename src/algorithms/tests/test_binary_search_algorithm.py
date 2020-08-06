import unittest

try:
    from coding_problems.src.algorithms.binary_search_algorithm import \
        binary_search
except ImportError as e:
    from coding_problems.src.algorithms.answers.binary_search_algorithm \
        import binary_search


class Test_Binary_Search(unittest.TestCase):

    def test_error_with_target_empty(self):
        with self.assertRaises(Exception):
            binary_search(None, [1, 2, 3])

    def test_error_with_numlist_empty(self):
        with self.assertRaises(Exception):
            binary_search(1, None)

    def test_error_with_both_empty(self):
        with self.assertRaises(Exception):
            binary_search(None, None)

    def test_success_with_single_element(self):
        self.assertTrue(binary_search(2, [1, 2, 3, 4]))

    def test_success_with_mid_element(self):
        self.assertTrue(binary_search(3, [1, 2, 3, 4, 5, 6]))

    def test_success_with_corner_element(self):
        self.assertTrue(binary_search(4, [1, 2, 3, 4]))

    def test_success_with_first_element(self):
        self.assertTrue(binary_search(1, [1, 2, 3, 4]))

    def test_failure_with_no_element(self):
        self.assertFalse(binary_search(5, [1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
