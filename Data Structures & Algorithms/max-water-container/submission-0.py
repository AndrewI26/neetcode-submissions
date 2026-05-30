class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxWater = 0
        while l < r:
            lh, rh = heights[l], heights[r]
            maxWater = max(maxWater, (r - l) * min(lh, rh))

            if lh > rh:
                r -= 1
            elif rh > lh:
                l += 1
            else:
                l += 1
                r -= 1

        return maxWater 
            