import unittest

from coding_problems.src.arrays.reverse_array_inplace import reverse_array


class Test_Reverse_Array_Inplace(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse_array(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse_array(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse_array(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
