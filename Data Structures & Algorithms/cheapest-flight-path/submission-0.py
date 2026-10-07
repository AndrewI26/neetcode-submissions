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
        q = deque([(0, 0, src)]) # [(cost, stops, airport)]
        seen = set()

        min_cost = float("inf")
        while q:
            # print(q)
            cost, stops, ap = q.popleft()
            if ap in seen: continue
            if stops > k and ap != dst:
                continue
            
            if ap == dst:
                min_cost = min(cost, min_cost)
            
            for stop in paths[ap].keys():
                q.append((cost + paths[ap][stop], stops + 1, stop))
            
            seen.add(ap)

        
        return -1 if min_cost == float("inf") else min_cost
