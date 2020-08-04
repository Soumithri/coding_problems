import unittest

try:
    from coding_problems.src.hashes.palindrome_permutation import \
        has_palindrome_permutation
except ImportError as e:
    from coding_problems.src.hashes.answers.palindrome_permutation import \
        has_palindrome_permutation


class Test_Palindrome_Permutation(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
