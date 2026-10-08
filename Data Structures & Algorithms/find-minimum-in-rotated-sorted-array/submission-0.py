class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(l - r) <= 1:
                return min(nums[l], nums[r])

            mid = math.floor((l + r) / 2)
            mid_el = nums[mid]


            if mid_el > nums[l]:
                l = mid
            else:
                r = mid
        
        return nums[l]
        