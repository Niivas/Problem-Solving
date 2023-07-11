from collections import deque, defaultdict
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Create a queue to perform BFS traversal of the binary tree
        queue = deque([root])
        # Create a graph to store the connections between nodes
        graph = defaultdict(list)

        # Construct the graph using BFS traversal of the tree
        while queue:
            cur_node = queue.popleft()
            if cur_node.left:
                # Add an edge between the current node and its left child
                graph[cur_node.val].append(cur_node.left.val)
                graph[cur_node.left.val].append(cur_node.val)
                # Add the left child to the queue for further traversal
                queue.append(cur_node.left)
            if cur_node.right:
                # Add an edge between the current node and its right child
                graph[cur_node.val].append(cur_node.right.val)
                graph[cur_node.right.val].append(cur_node.val)
                # Add the right child to the queue for further traversal
                queue.append(cur_node.right)
        
        # Perform BFS starting from the target node to find nodes at distance k
        queue.append((target.val, k))
        # Create a set to track visited nodes
        visited = {target.val}
        # Initialize a list to store nodes at distance k
        ans = []

        while queue:
            cur_node, dist = queue.popleft()
            if dist == 0:
                # Add the current node to the result list if the distance is k
                ans.append(cur_node)
                continue
            for node in graph[cur_node]:
                if node not in visited:
                    # Add neighbors of the current node to the queue for further traversal
                    queue.append((node, dist - 1))
                    visited.add(node)
        
        # Return the list of nodes at distance k
        return ans