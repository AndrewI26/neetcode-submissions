class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 
        s = s.upper()
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            print(s[l], s[r])
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True