class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        profit = 0
        for i in range(len(prices) - 1):
            a = prices[i]
            b = prices[i + 1]
            temp = b - a
            if temp > 0:
                profit += temp
        return profit
