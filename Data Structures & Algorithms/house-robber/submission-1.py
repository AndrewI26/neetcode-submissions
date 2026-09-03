class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max amt of money from nums[i:]
        # take = nums[i] + dp[i - 2]
        # leave = dp[i-1]
        # dp[i] = max(take, leave)
        len_nums = len(nums)
        
        prev, curr = 0, 0

        for num in nums:
            take = num + prev
            leave = curr
            temp = max(take, leave)

            prev = curr
            curr = temp
        
        
        return curr