class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = true if the substring s[i..j] is a palindrome
        # dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
        # 

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        longest = s[0]
        for j in range(1, len(s)):
            for i in range(j):
                is_palindrome = s[i] == s[j] and (i + 1 == j or dp[i+1][j-1])
                dp[i][j] = is_palindrome
                if is_palindrome and len(longest) < j - i + 1:
                    longest = s[i:j+1]

        
        return longest

            