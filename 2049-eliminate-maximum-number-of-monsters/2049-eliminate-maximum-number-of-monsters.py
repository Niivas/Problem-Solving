from heapq import heappush, heappop
class Solution:
    @staticmethod
    def eliminateMaximum(dist: List[int], speed: List[int]) -> int:
        minHeap = []
        for i, item in enumerate(dist):
            heappush(minHeap, item / speed[i])
        count = 0
        while minHeap:
            if count >= heappop(minHeap):
                return count
            count += 1
        return count
