# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    @staticmethod
    def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

            # Step 1: Copy Nodes
        cur = head
        while cur:
            nxt = cur.next  # Store the next node in the original list
            cur.next = Node(cur.val)  # Create a copy of the current node and insert it after the original
            cur.next.next = nxt  # Update the new node's 'next' to point to the original's 'next'
            cur = nxt  # Move to the next original node

        # Step 2: Copy Random Pointers
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next  # Update the random pointer of the copy
            cur = cur.next.next  # Move to the next original node

        # Step 3: Separate Two Parts
        second = cur = head.next  # 'second' points to the head of the copied list
        while cur.next:
            head.next = cur.next  # Disconnect original list node from copied list node
            head = head.next  # Move to the next original list node
            cur.next = head.next  # Disconnect copied list node from original list node
            cur = cur.next  # Move to the next copied list node
        head.next = None  # Set the 'next' of the last node in the original list to None

        return second  # Return the head of the copied list
