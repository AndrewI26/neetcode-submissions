class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 1
        f = nums[nums[s]]        
        while f != s:
            s = nums[nums[s]]
            f = nums[nums[nums[f]]]
        
        return nums[f]