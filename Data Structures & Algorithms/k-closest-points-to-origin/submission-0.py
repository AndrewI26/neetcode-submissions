import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []

        for x, y in points:
            dis = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(closest, (dis, [x, y]))
        
        res = []
        for i in range(k):
            closest_point = heapq.heappop(closest)
            res.append(closest_point[1])
        
        return res
