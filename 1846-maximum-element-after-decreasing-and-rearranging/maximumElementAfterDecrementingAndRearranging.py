class Solution:
    @staticmethod
    def maximumElementAfterDecrementingAndRearranging(A):  # -> int:
        """
        :type A: List[int]
        :param A:
        :return:
        """

        A.sort()  # O(nlogn)
        ans = 0
        for a in A:
            ans = min(ans + 1, a)
        return ans
