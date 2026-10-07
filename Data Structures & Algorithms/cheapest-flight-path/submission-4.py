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
        while q:
            cost, stops, ap, seen = q.popleft()
            if ap in seen: continue
            if stops > k:
                continue
            
            if ap == dst:
                min_cost = min(cost, min_cost)
            
            if ap not in paths: continue
            for stop in paths[ap].keys():
                new_seen = seen.copy()
                new_seen.add(ap)
                q.append((cost + paths[ap][stop], stops + 1, stop, new_seen))
            

        
        return -1 if min_cost == float("inf") else min_cost
