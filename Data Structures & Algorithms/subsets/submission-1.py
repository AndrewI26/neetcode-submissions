class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            subsets += [[*subset, num] for subset in subsets]

        return subsets