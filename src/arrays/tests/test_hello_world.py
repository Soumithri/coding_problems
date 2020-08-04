import unittest
from coding_problems.src.arrays.sample_test import test


class HelloWorldTest(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(test(), True)


if __name__ == '__main__':
    unittest.main()
