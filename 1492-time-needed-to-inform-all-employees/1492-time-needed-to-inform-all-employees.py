class Solution:
    @staticmethod
    def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        tree = defaultdict(list)
        # Build the tree by assigning each employee to their respective manager
        for idx, value in enumerate(manager):
            if idx != headID:
                tree[value].append(idx)

        total_time = 0
        queue = deque([(headID, informTime[headID])])

        # Perform breadth-first search traversal of the tree
        while queue:
            cur_employee, cur_time = queue.popleft()
            # Update the maximum time required to inform all employees
            total_time = max(total_time, cur_time)
            # Visit each subordinate of the current employee
            for subordinate in tree[cur_employee]:
                if tree[subordinate]:
                    # Calculate the time required to inform the subordinate and enqueue them
                    queue.append((subordinate, cur_time + informTime[subordinate]))

        return total_time
