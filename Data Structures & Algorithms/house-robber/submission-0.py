class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max amt of money from nums[i:]
        # take = nums[i] + dp[i - 2]
        # leave = dp[i-1]
        # dp[i] = max(take, leave)
        len_nums = len(nums)
        dp = [0] * len_nums
        dp[0] = nums[0]

        for i in range(1, len_nums):
            take = nums[i] + dp[i-2]
            leave = dp[i-1]
            dp[i] = max(take, leave)
        
        return dp[len_nums - 1]