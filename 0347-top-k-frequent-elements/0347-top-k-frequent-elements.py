class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)
        ans,maxheap = [],[]
        for key in counter:
            heapq.heappush(maxheap,(-counter[key],-key))
        
        i = 0

        while i<k:
            value,key = heapq.heappop(maxheap)
            ans.append(-key)
            i+=1
        
        return ans