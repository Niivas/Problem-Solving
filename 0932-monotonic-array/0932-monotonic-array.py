class Solution:
    @staticmethod
    def isMonotonic(nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        isIncreasing = True
        isDecreasing = True
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                isDecreasing = False
            elif nums[i]<nums[i-1]:
                isIncreasing = False
        return isIncreasing or isDecreasing
