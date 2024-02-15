import heapq
from typing import List

class Solution:
    @staticmethod
    def findKthLargest(nums: List[int], k: int) -> int:
        ans = 0
        maxHeap = []

        for i in nums:
            heapq.heappush(maxHeap,-i)

        while k:
            ans = heapq.heappop(maxHeap)
            k-=1
        return -ans
