class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = math.floor((l + r) / 2)

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            
        
        return res

