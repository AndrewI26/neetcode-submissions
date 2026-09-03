class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        else:
            subsets = self.subsets(nums[1:])
            return [[nums[0]] + subset for subset in subsets] + subsets