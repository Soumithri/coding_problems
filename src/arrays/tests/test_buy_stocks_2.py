import unittest

try:
    from coding_problems.src.arrays.buy_stocks_2 import maxProfit
except ImportError as e:
    from coding_problems.src.arrays.answers.buy_stocks_2 import maxProfit


class TestBuyStocks2(unittest.TestCase):

    def test_for_one_element_in_prices(self):
        prices = [1]
        self.assertEqual(0, maxProfit(prices))

    def test_for_success_case_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(7, maxProfit(prices))

    def test_for_increasing_prices(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(4, maxProfit(prices))

    def test_for_decreasing_prices(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(0, maxProfit(prices))


if __name__ == "__main__":
    unittest.main(verbosity=2)
