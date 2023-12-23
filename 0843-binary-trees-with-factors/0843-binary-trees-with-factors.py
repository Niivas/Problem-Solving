class Solution:
    @staticmethod
    def numFactoredBinaryTrees(arr: List[int]) -> int:
        arr.sort()
        dp = {}
        for i, item in enumerate(arr):
            dp[item] = 1
            for j in range(i):
                if item % arr[j] == 0 and item // arr[j] in dp:
                    dp[item] += dp[arr[j]] * dp[item // arr[j]]
        return sum(dp.values()) % (10 ** 9 + 7)
