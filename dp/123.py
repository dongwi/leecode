from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 2
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        # dp[i][k][0] 表示第i天，总共进行了k次交易，并且没有持有股票
        # dp[i][k][1] 表示第i天，总共进行了k次交易，且持有股票
        # 所谓一次交易，指的是一次买和卖
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')
        for j in range(1, k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[- 1][-1][0]
