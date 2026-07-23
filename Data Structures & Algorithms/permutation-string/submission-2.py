class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        freq_s1 = {}
        for char in s1:
            freq_s1[char] = freq_s1.get(char, 0) + 1
        freq_s2 = {}
        for char in s2[0:len(s1)]:
            freq_s2[char] = freq_s2.get(char, 0) + 1

        if freq_s1 == freq_s2: return True
        r = len(s1)
        while r < len(s2):
            print(freq_s1, freq_s2)
            freq_s2[s2[r]] = freq_s2.get(s2[r], 0) + 1
            if freq_s2[s2[r-len(s1)]] > 1:
                freq_s2[s2[r - len(s1)]] -= 1
            else:
                del freq_s2[s2[r - len(s1)]]

            if freq_s1 == freq_s2: return True
            r += 1

        return False