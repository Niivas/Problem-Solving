from heapq import heappush, heappop
class Solution:
    @staticmethod
    def eliminateMaximum(dist: List[int], speed: List[int]) -> int:
        minHeap = []
        for i in range(len(dist)):
            heappush(minHeap, dist[i] / speed[i])
        count = 0
        while minHeap:
            if count >= heappop(minHeap):
                return count
            count += 1
        return count