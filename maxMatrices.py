from typing import List


def countSubmatrices(grid: List[List[int]], k: int) -> int:
    n, m = len(grid), len(grid[0])
    ans = 0
    i, j = 0, 0
    curSum = 0
    while i < n and j < m:
        curSum += grid[i][j]
        if i == n - 1 or j == m - 1:
            if curSum <= k:
                ans += 1

def prefixSumMatrix(Mat):
    n = len(Mat)
    m = len(Mat[0])
    prefixSum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            prefixSum[i][j] = prefixSum[i + 1][j] + prefixSum[i][j + 1] - prefixSum[i][j] + Mat[i][j]

    return prefixSum

print(prefixSumMatrix([[7,2,9],[1,5,0],[2,6,6]]))
