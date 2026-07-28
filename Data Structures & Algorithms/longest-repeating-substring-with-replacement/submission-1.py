class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        longest = 1
        for r in range(len(s)):
            print(freq, l, r)
            freq[s[r]] = freq.get(s[r], 0) + 1

            if max(freq.values()) >= sum(freq.values()) - k:
                longest = max(longest, r - l + 1)

            l = 0

        return longest