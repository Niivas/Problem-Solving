# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
        @staticmethod
        def findInMountainArray(target, A):
            n = A.length()
            # find index of peak
            l, r = 0, n - 1
            while l < r:
                m = (l + r) // 2
                if A.get(m) < A.get(m + 1):
                    l = peak = m + 1
                else:
                    r = m
            # find target in the left of peak
            l, r = 0, peak
            while l <= r:
                m = (l + r) // 2
                if A.get(m) < target:
                    l = m + 1
                elif A.get(m) > target:
                    r = m - 1
                else:
                    return m
            # find target in the right of peak
            l, r = peak, n - 1
            while l <= r:
                m = (l + r) // 2
                if A.get(m) > target:
                    l = m + 1
                elif A.get(m) < target:
                    r = m - 1
                else:
                    return m
            return -1
