from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        paths = {}
        for start, end, cost in flights:
            if start in paths:
                paths[start][end] = cost
            else:
                paths[start] = {}       
                paths[start][end] = cost

        q = deque([(0, 1, src, set())]) # [(cost, stops, airport)]

        k += 2

        min_cost = float("inf")
        def backtrack(cost: int, ap: int, seen: set[int]):
            nonlocal min_cost
            if ap in seen:
                return
            if len(seen) > k:
                return
            if ap == dst:
                min_cost = min(min_cost, cost)
                return
            
            if ap not in paths: 
                return
            
            for stop in paths[ap].keys():
                seen.add(ap)
                backtrack(cost + paths[ap][stop], stop, seen)
                seen.remove(ap)

        backtrack(0, src, set())
        return -1 if min_cost == float("inf") else min_cost
