import math


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        动态规划的实现，dp[i]为包含nums[i]时，最大的子序列
        递推方程为：dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0
                  dp[i] = nums[i] if dp[i-1] <= 0
        时间复杂度为：O(N)
        :param nums:
        :return:
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dp[i - 1], 0)
            res = max(res, dp[i])
        return res

    def maxSubArrayDivide(self, nums: list[int]) -> int:
        """
        分治的方式求解
        :param nums:
        :return:
        """

        def cross(left, mid, right):
            """
            贪心算法，分别求左序列和右序列的最大值，然后加起来求和
            :param left:
            :param mid:
            :param right:
            :return:
            """
            left_sum = nums[mid]
            right_sum = nums[mid + 1]
            sum = 0
            for i in range(mid, left - 1, -1):
                sum += nums[i]
                left_sum = max(left_sum, sum)

            sum = 0
            for i in range(mid + 1, right + 1):
                sum += nums[i]
                right_sum = max(right_sum, sum)

            return left_sum + right_sum

        def helper(left, right):
            if left == right:
                return nums[left]
            mid = (left + right) / 2
            # 这里有点像二叉树的后序遍历
            left_sum = helper(left, mid)
            right_sum = helper(mid + 1, right)
            mid_sum = cross(left, mid, right)
            return max(max(left_sum, right_sum), mid_sum)

        return helper(0, len(nums) - 1)
