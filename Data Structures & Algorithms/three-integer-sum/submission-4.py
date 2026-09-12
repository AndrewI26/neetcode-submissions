class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, first_num in enumerate(nums):
            target = -first_num

            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr_sum = nums[l] + nums[r]

                if curr_sum == target:
                    result = [first_num, nums[l], nums[r]]
                    if result not in res: res.append(result)
                    l += 1
                    r -= 1
                elif curr_sum > target:
                    r -= 1
                else:
                    l += 1
            
        return res