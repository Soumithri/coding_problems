
def maxProfit(prices):
    buy, sell, length = 0, 0, len(prices)
    max_profit = 0

    i = 0
    while i < length-1:
        while i < length-1 and prices[i+1] <= prices[i]:
            i += 1
        buy = prices[i]
        while i < length-1 and prices[i+1] >= prices[i]:
            i += 1
        sell = prices[i]
        max_profit += sell - buy
    return max_profit
