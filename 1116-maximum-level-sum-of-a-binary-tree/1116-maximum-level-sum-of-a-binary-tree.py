from collections import deque
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])  # Initialize a queue with the root node
        max_sum = -math.inf  # Initialize the maximum sum to negative infinity
        max_level = 0  # Initialize the level with the maximum sum
        cur_level = 0  # Initialize the current level

        while queue:
            cur_level += 1  # Increment the current level
            cur_level_sum = 0  # Initialize the sum of values at the current level
            n = len(queue)  # Get the number of nodes at the current level

            for _ in range(n):
                cur_node = queue.popleft()  # Remove the first node from the left of the queue
                cur_level_sum += cur_node.val  # Add the value of the current node to the current level sum

                if cur_node.left:
                    queue.append(cur_node.left)  # Add the left child to the queue

                if cur_node.right:
                    queue.append(cur_node.right)  # Add the right child to the queue

            if cur_level_sum > max_sum:  # Check if the current level sum is greater than the maximum sum
                max_level = cur_level  # Update the level with the maximum sum
                max_sum = cur_level_sum  # Update the maximum sum

        return max_level  # Return the level with the maximum sum
