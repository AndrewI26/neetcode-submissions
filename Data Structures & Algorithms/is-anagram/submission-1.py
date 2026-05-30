class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        for letter in s:
            freqS[letter] = freqS.get(letter, 0) + 1
        
        for letter in t:
            if letter in freqS:
                freqS[letter] -= 1
            else:
                return False
        
        for count in freqS.values():
            if count != 0:
                return False
        return True
