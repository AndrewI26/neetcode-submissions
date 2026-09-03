class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def helper(s, wordDict):
            if s == "": return True
            for word in wordDict:
                if s[:len(word)] == word:
                    attempt = helper(s[len(word):], wordDict)
                    if attempt:
                        return True
            return False
        
        return helper(s, wordDict)