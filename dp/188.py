from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        if k >= n // 2:  # 退化为不限制交易次数
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:  # 初始化i=0的情况
                    dp[0][j][1] = -prices[0]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[-1][-1][0]
