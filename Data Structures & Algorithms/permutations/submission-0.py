class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums_left: set[int], cur_path: list[int]):
            print(f"nums_left: {nums_left}, cur_path: {cur_path}, not nums_left: {not nums_left}")
            if not nums_left:
                res.append(cur_path.copy())
                return
            
            for num in nums_left.copy():
                nums_left.remove(num)
                cur_path.append(num)
                backtrack(nums_left, cur_path)
                nums_left.add(num)
                cur_path.pop()
            
        backtrack(set(nums), [])
        return res
