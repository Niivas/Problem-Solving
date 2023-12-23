class Solution:
    @staticmethod
    def maximumScore(nums: List[int], k: int) -> int:

        n = len(nums)
        left, right = k, k
        result = nums[k]
        minVal = nums[k]
        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] < nums[right + 1]:
                right += 1
            else:
                left -= 1
            minVal = min(minVal, nums[left], nums[right])
            result = max(result, minVal * (right - left + 1))
        return result
