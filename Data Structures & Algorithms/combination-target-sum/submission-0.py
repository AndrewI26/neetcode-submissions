class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(cur_sum: int, path: List[int]):
            if cur_sum > target:
                return

            if cur_sum == target:
                sorted_p = sorted(path)
                if sorted_p not in res:
                    res.append(sorted_p.copy())
                return
            
            for num in nums:
                path.append(num)
                backtrack(cur_sum + num, path)
                path.pop()
            
        backtrack(0, [])
        return res