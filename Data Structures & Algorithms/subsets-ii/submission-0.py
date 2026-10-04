class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(cur_path: list[int]):
            if not nums: 
                if cur_path not in res:
                    res.append(cur_path.copy())
                return
            
            el = nums.pop()
            backtrack(cur_path)

            cur_path.append(el)
            backtrack(cur_path)

            nums.append(el)
            cur_path.pop()
        
        backtrack([])
        return res