from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # If the length of 'nums' is less than 2k + 1, return a list of -1's
        if 2 * k + 1 > n:
            return [-1] * n
        
        # If k is 0, return 'nums' as it is
        if k == 0:
            return nums
        
        total = 2 * k + 1
        start, end = 0, 2 * k
        runningSum = sum(nums[start : end + 1])
        kRadiusAvgs = []
        kRadiusAvgs.append(runningSum // total)
        
        end += 1
        while end < n:
            runningSum += (nums[end] - nums[start])
            curAvg = runningSum // total
            kRadiusAvgs.append(curAvg)
            start += 1
            end += 1
        
        # Return the final list containing -1's, averages, and -1's
        return [-1] * k + kRadiusAvgs + [-1] * k