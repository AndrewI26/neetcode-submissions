'''
[2,1,5,1,5,3]
target = 4

1 1 3 1 1
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        min_len = 0
        cur_sum = sum(nums)
        while l <= r:
            if cur_sum >= target:
                min_len = r - l + 1 

            if nums[l] > nums[r]:
                cur_sum -= nums[r]
                r -= 1
            else:
                cur_sum -= nums[l]
                l += 1

        return min_len 

        

        