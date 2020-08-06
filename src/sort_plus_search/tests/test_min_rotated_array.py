import unittest

try:
    from coding_problems.src.sort_plus_search.min_rotated_array import find_min
except ImportError as e:
    from coding_problems.src.sort_plus_search.answers.min_rotated_array \
        import find_min


class Test_Min_Rotated_Array(unittest.TestCase):

    def test_with_no_input(self):
        self.assertEqual(-1, find_min(None))

    def test_with_two_inputs(self):
        self.assertEqual(1, find_min([1, 2]))

    def test_with_three_inputs(self):
        self.assertEqual(1, find_min([1, 2, 3]))

    def test_success_1(self):
        self.assertEqual(0, find_min([4, 5, 6, 7, 0, 1, 2]))

    def test_success_2(self):
        self.assertEqual(1, find_min([3, 4, 5, 1, 2]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
