import heapq
from collections import Counter
from typing import List

class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number in the list
        counter = Counter(nums)

        # Initialize an empty list for the answer and a max heap
        top_k_frequent = []
        max_heap = []

        # Push the frequency and negated number (-frequency, -number) into the max heap
        for num, freq in counter.items():
            heapq.heappush(max_heap, (-freq, -num))

        i = 0
        # Pop the top k elements from the max heap and append the negated number to the answer list
        while i < k:
            freq, num = heapq.heappop(max_heap)
            top_k_frequent.append(-num)
            i += 1

        return top_k_frequent
