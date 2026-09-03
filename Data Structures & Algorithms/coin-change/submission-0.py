"""
dp[i] = fewest # coins to make i
take1 = dp[i - 1]
dp[i] = max(take1, take5, take10)
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        
        for i in range(1, amount+1):
            min_coins = float("inf")
            for coin in coins:
                amt_left = i - coin
                coins_for_amt = dp[amt_left]
                if amt_left >= 0 and coins_for_amt != -1:
                    min_coins = min(coins_for_amt + 1, min_coins)
            dp[i] = min_coins if min_coins != float("inf") else -1
            print(dp)
        
        return dp[amount]