class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 1
        f = nums[nums[s]]        
        while True:
            s = nums[nums[s]]
            f = nums[nums[nums[f]]]
            if s == f:
                break
        
        return nums[f]