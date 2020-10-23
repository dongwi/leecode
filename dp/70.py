class Solution:
    def climbStairs(self, n: int) -> int:
        # 其实就是一个斐波拉契数列，如果题目中新增一次可以跨3不的楼梯，则递推公式如何处理
        # 如果要求空间复杂度为1，那么如何优化？
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        if n > 2:
            # range是前包后不包，下面range的输出为 2 .. n-1 当时range(2,2)是没有输出的
            for i in range(2, n):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]

    def climbStarisOpt(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        x = 1
        y = 2
        for _ in range(2, n):
            x, y = y, x + y
        return y

    def climStaris3(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        dp = [0] * n
        # 当有三种爬楼方式时
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4
        for i in range(3, n):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n - 1]

if __name__ == '__main__':
    Solution().climbStairs(3)
