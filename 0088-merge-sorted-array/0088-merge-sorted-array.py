class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if nums1 is empty, replace it with nums2
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        # if nums2 is empty, do nothing
        elif n == 0:
            pass
        else:
            p1, p2, cur = m-1, n-1, m+n-1
            # iterate from the end of the two arrays and add elements to nums1
            while p2 >= 0:
                # if the current element in nums2 is larger, add it to nums1
                if nums2[p2] >= nums1[p1]:
                    nums1[cur] = nums2[p2]
                    p2 -= 1
                # otherwise, add the current element from nums1 to nums1
                else:
                    nums1[cur] = nums1[p1]
                    p1 -= 1
                # move the pointer to the next position in nums1
                cur -= 1
                # if we have added all the elements from nums1, add the remaining elements from nums2
                if p1 < 0:
                    while p2 >= 0:
                        nums1[cur] = nums2[p2]
                        p2 -= 1
                        cur -= 1