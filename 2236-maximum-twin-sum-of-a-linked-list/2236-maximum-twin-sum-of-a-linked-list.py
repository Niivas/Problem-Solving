class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = -math.inf  # Initialize ans with negative infinity

        slow, fast = head, head.next  # Initialize slow and fast pointers

        while fast.next:  # Move the fast pointer at twice the speed of the slow pointer
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next  # Get the second half of the linked list
        temp, prev = head2, None

        while temp:  # Reverse the second half of the linked list
            cur = temp
            temp = temp.next
            cur.next = prev
            prev = cur

        while prev:  # Calculate the maximum sum of pairs
            ans = max(ans, head.val + prev.val)
            head = head.next
            prev = prev.next

        return ans
