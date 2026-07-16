from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            min_price = min(i, min_price)
            profit = i - min_price
            max_profit = max(profit, max_profit)
        return max_profit
