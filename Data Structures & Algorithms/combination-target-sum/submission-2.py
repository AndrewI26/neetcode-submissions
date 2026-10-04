class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(cur_sum: int, path: List[int]):
            if cur_sum > target:
                return

            if cur_sum == target:
                if path not in res:
                    res.append(path.copy())
                return
            
            for num in nums:
                path[num] += 1
                backtrack(cur_sum + num, path)
                path[num] -= 1
            
        backtrack(0, [0 for i in range(33)])

        result = []
        for arr in res:
            a = []
            for i, el in enumerate(arr):
                for _ in range(el):
                    a.append(i)
                
            result.append(a)

        return result