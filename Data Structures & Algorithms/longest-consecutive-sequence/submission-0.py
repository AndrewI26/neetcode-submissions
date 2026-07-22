class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLen = 1

        for num in nums:
            length = 1
            while num + length in seen:
                length += 1

            maxLen = max(length, maxLen)
            seen.add(num)

        return maxLen

