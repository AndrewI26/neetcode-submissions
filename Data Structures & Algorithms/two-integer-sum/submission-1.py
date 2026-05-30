class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        num_to_index = {}
        for i, num in enumerate(nums):
            paired_num = target - num
            if paired_num in seen:
                return [num_to_index[paired_num], i]
            
            seen.add(num)
            num_to_index[num] = i