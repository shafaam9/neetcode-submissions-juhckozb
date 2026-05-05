import math, heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []
        res = []
        for x, y in points:
            dist = ((x ** 2) + (y ** 2)) ** 0.5
            heapq.heappush(self.heap, (-dist, (x,y)))
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        
        for distance, points in self.heap:
            res.append(points)
        return res