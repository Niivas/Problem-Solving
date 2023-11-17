class Solution:
        @staticmethod
        def shortestBridge(A: List[List[int]]) -> int:
            bound= set()
            dire = [(1,0),(-1,0),(0,1),(0,-1)]
            m, n = len(A), len(A[0])
            # get root of islanda
            def getfirst():
                for i in range(m):
                    for j in range(n):
                        if A[i][j] == 1:
                            return i,j
            # get boundary of islanda
            def dfs(i,j):
                A[i][j] = -1
                for d in dire:
                    x,y = i+d[0],j+d[1]
                    if 0 <= x<m and 0 <= y < n:
                        if A[x][y] == 0:
                            bound.add((i,j))
                        elif A[x][y] == 1:
                            dfs(x,y)
            i,j = getfirst()
            dfs(i,j)
            # BFS to find next island
            step = 0
            while bound:
                new = []
                for i,j in bound:
                    for d in dire:
                        x,y = i+d[0],j+d[1]
                        if 0 <= x < m and 0 <= y < n:
                            if A[x][y] == 1:
                                return step
                            elif A[x][y] ==0:
                                A[x][y] = -1
                                new.append((x,y))
                step += 1
                bound = new
            