class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = defaultdict(list)

        for i,val in enumerate(nums):
            hm[val].append(i)

        ans = 0
        for idxs in hm.values():
            ans += (len(idxs)*(len(idxs)-1))//2
        
        return ans
