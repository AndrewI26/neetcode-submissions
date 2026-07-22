class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        longest = 1
        
        for r in range(1, len(s)):
            l = r - 1
            contains = set()
            contains.add(s[r])
            while l >= 0:
                if not s[l] in contains:
                    contains.add(s[l])
                else:
                    longest = max(r - l, longest)
                    break
                l -= 1
    
        return longest