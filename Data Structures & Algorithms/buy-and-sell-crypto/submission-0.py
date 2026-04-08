class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        windowStart = 0
        profit = 0
        res = 0

        for windowEnd in range(1, len(prices)):
            if prices[windowEnd] <= prices[windowStart]:
                windowStart = windowEnd 
            else:
                profit = max(profit, prices[windowEnd] - prices[windowStart])
        return profit




        