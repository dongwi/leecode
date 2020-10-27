class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # dp的含义为，包含的当前n时，对应的上升子序列的长度
        dp = [0] * len(nums)
        res = 1
        if not nums:
            return 0
        # 从这里可以看出，时间复杂度为O(n)
        for i in range(len(nums)):
            # 向前查找第一个小于当前值的dp
            for j in range(i - 1, -1, -1):
                # 这里一定是将所有的前序都比较完
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] == 0:
                dp[i] = 1
            res = max(res, dp[i])
        return res
