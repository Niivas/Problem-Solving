class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums)>1:
            slow = nums[0]
            fast = nums[slow]

            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            
            fast = 0

            while fast != slow:
                fast = nums[fast]
                slow = nums[slow]
            return slow
        return -1
