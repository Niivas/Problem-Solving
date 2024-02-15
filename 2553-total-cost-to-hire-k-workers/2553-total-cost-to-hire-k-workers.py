import heapq

class Solution:
    @staticmethod
    def totalCost(costs, k, candidates):
        left = 0  # left index of the costs list
        right = len(costs) - 1  # right index of the costs list
        left_pq = []  # priority queue to store costs from the left
        right_pq = []  # priority queue to store costs from the right

        total_cost = 0  # variable to store the total cost

        while k > 0:
            # Push costs from the left into left_pq until it has candidates number of elements or left > right
            while len(left_pq) < candidates and left <= right:
                heapq.heappush(left_pq, costs[left])
                left += 1

            # Push costs from the right into right_pq until it has candidates number of elements or left > right
            while len(right_pq) < candidates and left <= right:
                heapq.heappush(right_pq, costs[right])
                right -= 1

            t1 = left_pq[0] if left_pq else float('inf')  # get the smallest cost from left_pq or float('inf')
            t2 = right_pq[0] if right_pq else float('inf')  # get the smallest cost from right_pq or float('inf')

            if t1 <= t2:
                total_cost += t1
                heapq.heappop(left_pq)
            else:
                total_cost += t2
                heapq.heappop(right_pq)

            k -= 1

        return total_cost
