import unittest

try:
    from coding_problems.src.hashes.two_sum import twoSum
except ImportError as e:
    from coding_problems.src.hashes.answers.two_sum import twoSum


class Test_Two_Sum(unittest.TestCase):

    def test_short_target(self):
        result = twoSum([2, 4], 1)
        self.assertFalse(result)

    def test_long_target(self):
        result = twoSum([2, 4], 6)
        self.assertTrue(result)

    def test_one_num_half_target_length(self):
        result = twoSum([3, 8], 6)
        self.assertFalse(result)

    def test_two_nums_half_target_length(self):
        result = twoSum([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = twoSum([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_num(self):
        result = twoSum([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_num(self):
        result = twoSum([6], 6)
        self.assertFalse(result)

    def test_no_nums(self):
        result = twoSum([], 2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
