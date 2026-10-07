class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i: int, cur_sum: int, cur_list: list[int]):
            if cur_sum > target:
                return

            if i == len(candidates):
                if cur_sum == target and cur_list not in res:
                    res.append(cur_list.copy())
                return
            
            if i > 0 and candidates[i - 1] == candidates[i]:
                backtrack(i + 1, cur_sum, cur_list)

            backtrack(i + 1, cur_sum, cur_list)

            cur_list.append(candidates[i])
            backtrack(i + 1, cur_sum + candidates[i], cur_list)
            cur_list.pop()

        backtrack(0, 0, [])
        return res
            