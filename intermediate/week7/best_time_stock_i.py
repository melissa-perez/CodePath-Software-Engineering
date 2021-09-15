# Author: Melissa Perez
# Date: --/--/--
# Description:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_length = len(prices)
        # guaranteed len at least 1
        min_price = prices[0]
        max_profit = 0

        for i in range(1, prices_length):

            if prices[i] < min_price:
                min_price = prices[i]
            else:
                selling_price = prices[i] - min_price
                max_profit = max_profit if max_profit > selling_price else selling_price

        return max_profit