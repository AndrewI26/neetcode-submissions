'''
zxyzxy
   |
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len <= 1: return s_len

        longest = 1
        chars = set(s[0])
        l = 0
        for r in range(1, s_len):
            while s[r] in chars and l < r:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest



