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

        print(paths)
        q = deque([(0, 1, src)]) # [(cost, stops, airport)]
        seen = set()

        k += 2

        min_cost = float("inf")
        while q:
            cost, stops, ap = q.popleft()
            if ap in seen: continue
            if stops > k:
                continue
            
            if ap == dst:
                min_cost = min(cost, min_cost)
            
            if ap not in paths: continue
            for stop in paths[ap].keys():
                q.append((cost + paths[ap][stop], stops + 1, stop))
            
            seen.add(ap)

        
        return -1 if min_cost == float("inf") else min_cost
