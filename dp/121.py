from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i]表示在第i天进行交易时，获得第最大利润
        if not prices or len(prices) == 1:
            return 0
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = prices[i] - min(prices[:i])
        return max(dp)
