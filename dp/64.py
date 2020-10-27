from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 特殊情况优先考虑
        if not grid:
            return 0
        # m行，n列的举证
        m = len(grid)
        n = len(grid[0])
        # dp定义为，从grid[0][0] 到dp[i][j]的最小路径和
        # 递推方程为：dp[i][j]=min(dp[i][j-1], dp[i-1][j]) + grid(i, j)
        # 边界条件，当i = 0时，没有没有i-1,当j=0时，没有j-1
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0:
                    dp[0][j] = dp[0][j - 1] + grid[0][j]
                elif j == 0:
                    dp[i][0] = dp[i-1][0] + grid[i][0]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
