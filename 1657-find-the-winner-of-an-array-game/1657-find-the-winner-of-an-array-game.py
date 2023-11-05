from collections import deque
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr = deque(arr)
        i,j = 0,1
        win_count = 0
        if k>=len(arr):
            return max(arr)
        while win_count<k:
            if arr[i]<arr[j]:
                win_count =1
                arr.append(arr.popleft())
            else:
                arr[i],arr[j] = arr[j],arr[i]
                win_count +=1
                arr.append(arr.popleft())
        return arr[0]