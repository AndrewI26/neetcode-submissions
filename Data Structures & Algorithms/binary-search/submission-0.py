class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = math.floor((l + r) / 2)
            mid_el = nums[mid]

            if target == mid_el:
                return mid
            elif target > mid_el:
                l = mid + 1
            else:
                r = mid - 1

        return -1