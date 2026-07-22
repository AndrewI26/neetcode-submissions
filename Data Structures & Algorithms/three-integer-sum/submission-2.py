class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # -4, -1, -1, 0, 1, 2

        l, r = 0, len(nums) - 1
        for i, num in enumerate(nums):
            while l < r:
                currSum = num + nums[l] + nums[r]
                if l == i:
                    break
                if r == i:
                    break
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
            l = 0
            r = len(nums) - 1


        return (list(set(res)))