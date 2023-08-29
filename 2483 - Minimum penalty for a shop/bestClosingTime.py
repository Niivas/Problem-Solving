class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = 0
        left_Ns = customers.count('N')
        right_Ys = 0
        n = len(customers)
        cur, prev = n, n
        while cur>-1:
            if cur == n:
                if prev>=left_Ns:
                    ans = cur
                    prev = left_Ns
            else:
                if customers[cur] == 'N':
                    left_Ns -=1
                else:
                    right_Ys +=1
                if left_Ns + right_Ys<=prev:
                    ans = cur
                    prev = left_Ns + right_Ys
            cur -=1
        return ans