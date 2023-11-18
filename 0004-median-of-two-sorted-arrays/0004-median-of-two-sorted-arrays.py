import sys


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        # Get lengths of the input arrays
        N1, N2 = len(nums1), len(nums2)

        # Ensure nums1 is the longer array
        if N1 < N2:
            nums1, N1, nums2, N2 = nums2, N2, nums1, N1

        # Initialize binary search bounds
        l, r = 0, N2 * 2

        # Perform binary search to find the median
        while l <= r:
            j = (l + r) >> 1
            i = N1 + N2 - j

            # Calculate left and right elements for each array
            L1 = -sys.maxsize - 1 if i == 0 else nums1[(i - 1) >> 1]
            L2 = -sys.maxsize - 1 if j == 0 else nums2[(j - 1) >> 1]
            R1 = sys.maxsize if i == 2 * N1 else nums1[i >> 1]
            R2 = sys.maxsize if j == 2 * N2 else nums2[j >> 1]

            # Update binary search bounds based on comparisons
            if L1 > R2:
                l = j + 1
            elif L2 > R1:
                r = j - 1
            else:
                # Median found, return the calculated median
                return (max(L1, L2) + min(R1, R2)) / 2.0
