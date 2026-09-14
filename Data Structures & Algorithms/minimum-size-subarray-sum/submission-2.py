'''
[2,1,5,1,5,3]
target = 4

cur_sum = 8

'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0

        min_len = float("inf")
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target and l <= r:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1


        return min_len if min_len != float("inf") else 0

        