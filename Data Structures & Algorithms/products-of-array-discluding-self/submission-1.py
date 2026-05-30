class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1 for i in range(len(nums))]
        suffix_prod = [1 for i in range(len(nums))]

        for i, num in enumerate(nums):
            if i == 0:
                prefix_prod[i] = num
                continue
            prefix_prod[i] *= prefix_prod[i-1] * num

        for j, num in enumerate(nums[::-1]):
            i = len(nums) - 1 - j
            if i == len(nums) - 1: 
                suffix_prod[i] = num
                continue
            suffix_prod[i] *= suffix_prod[i+1] * num

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix_prod[1])
            elif i == len(nums) - 1:
                res.append(prefix_prod[len(nums) - 2])
            else:
                res.append(prefix_prod[i-1] * suffix_prod[i+1])
        return res