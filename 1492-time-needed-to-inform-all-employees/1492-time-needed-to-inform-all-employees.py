class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        tree = defaultdict(list)

        for idx,value in enumerate(manager):
            if idx != headID:
                tree[value].append(idx)
        total_time = 0

        queue = deque([(headID,informTime[headID])])

        while queue:
            cur_employee,cur_time = queue.popleft()
            total_time = max(total_time,cur_time)
            for sub_ordinate in tree[cur_employee]:
                if tree[sub_ordinate]:
                    queue.append((sub_ordinate,cur_time+informTime[sub_ordinate]))
        
        return total_time