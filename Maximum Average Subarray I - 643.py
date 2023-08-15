from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k-1])
        left,right = 0,k-1
        maxSum = -float('inf')
        while right<len(nums):
            curSum += nums[right]
            if curSum>maxSum:
                maxSum = curSum
            curSum-= nums[left]
            left+=1
            right +=1
        return maxSum/k