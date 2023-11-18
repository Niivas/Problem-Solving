from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    @staticmethod
    def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
        valuesGreaterThanX = []
        valuesLesserThanX  = []

        start = head
        while start:
            if start.val >= x:
                valuesGreaterThanX.append(start.val)
            else:
                valuesLesserThanX.append(start.val)
            start = start.next

        ans = head

        for i in valuesLesserThanX:
            head.val = i
            head = head.next
        for i in valuesGreaterThanX:
            head.val = i
            head = head.next
        return  ans