from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_range(nums[0, len(nums) - 1]), self.rob_range(nums[1, len(nums)]))

    def rob_range(self, nums: List[int]) -> int:
        # dp数组的含义为：偷盗前i间房，能得到的最大利润
        # 递推方程为：dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[len(nums) - 1]
