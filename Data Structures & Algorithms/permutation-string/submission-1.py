class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_f = [0 for i in range(26)]
        for char in s1:
            s1_f[ord(char) % 26] += 1
        
        l = 0
        r = len(s1) - 1
        f = [0 for i in range(26)]

        for i in range(len(s1)):
            f[ord(s2[i]) % 26] += 1

        while r < len(s2):
            
            if f == s1_f:
                return True
            else:
                f[ord(s2[l]) % 26] -= 1
                if r < len(s2) - 1:
                    f[ord(s2[r+1]) % 26] += 1

            l += 1
            r += 1

        return False
