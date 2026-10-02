class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        hours = 0
        k = 0
        while l <= r:
            k = math.floor((l + r) / 2)

            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours == h:
                return k
            elif l == r:
                if hours < h:
                    return k
                else:
                    return k + 1
            elif hours < h:
                r = k - 1
            else:
                l = k + 1
            
            hours = 0

