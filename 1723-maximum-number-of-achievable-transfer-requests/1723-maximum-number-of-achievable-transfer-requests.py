class Solution:
    def __init__(self):
        self.max_requests = 0

    def helper(self, start, requests, indegree, n, count):
        # Base case: All requests have been processed
        if start == len(requests):
            # Check if all nodes have incoming request count 0
            for i in range(n):
                if indegree[i] != 0:
                    return
            # Update the maximum number of requests if the current count is higher
            self.max_requests = max(self.max_requests, count)
            return

        # Take the current request
        indegree[requests[start][0]] -= 1
        indegree[requests[start][1]] += 1
        self.helper(start + 1, requests, indegree, n, count + 1)

        # Not take the current request
        indegree[requests[start][0]] += 1
        indegree[requests[start][1]] -= 1
        self.helper(start + 1, requests, indegree, n, count)

    def maximumRequests(self, n, requests):
        # Initialize the incoming request count for each node
        indegree = [0] * n
        self.helper(0, requests, indegree, n, 0)
        return self.max_requests
        