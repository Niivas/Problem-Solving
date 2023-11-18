# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def hasCycle(head: Optional[ListNode]) -> bool:
        # check if the linked list is empty or has only one node
        if not head or not head.next:
            return False
        # initialize two pointers, slow and fast, to the head of the linked list
        slow, fast = head, head
        # loop through the linked list with a condition that checks if the fast pointer and its next node is not None
        while fast and fast.next:
            # check if the slow pointer is equal to the next node of the fast pointer, if True, it means that the
            # fast pointer has caught up with the slow pointer, and there is a cycle in the linked list. So,
            # return True.
            if slow == fast.next:
                return True
            # move the slow pointer one step forward, and the fast pointer two steps forward.
            slow = slow.next
            fast = fast.next.next
        # if the loop terminates, it means that there is no cycle in the linked list. So, return False.
        return False
