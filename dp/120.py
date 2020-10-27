class Solution:
    def minimumTotal(self, triangle) -> int:
        # dp[i][j] 为走到第i行，j列时的路径和
        n = len(triangle)
        # dp = [[0] * n] * n
        # 与下面这种dp生成的数组的形式不一样，一定要注意。上面生成的格式是相同的
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        return min(dp[n - 1])


if __name__ == '__main__':
    Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])