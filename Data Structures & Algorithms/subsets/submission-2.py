class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        search = []
        max_search = len(nums)
        def dfs(i):
            if i == max_search:
                subsets.append(search.copy())
                return
            
            dfs(i+1)
            search.append(nums[i])
            dfs(i+1)
            search.pop()

        dfs(0)
        return subsets