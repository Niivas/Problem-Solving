class Solution:
        def findArray(self, A):
            for i in range(len(A) - 1, 0, -1):
                A[i] ^= A[i - 1]
            return A
