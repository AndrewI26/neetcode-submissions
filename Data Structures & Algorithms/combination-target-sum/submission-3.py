'''
 2 
 5
'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i: int, cur_sum: int, cur_list: list[int]):
            if cur_sum > target:
                return
            if i == len(nums):
                if cur_sum == target:
                    res.append(cur_list.copy())
                return

            cur_list.append(nums[i])
            backtrack(i, cur_sum + nums[i], cur_list)
            cur_list.pop()

            backtrack(i + 1, cur_sum, cur_list)
        
        backtrack(0, 0, [])
        return res
                