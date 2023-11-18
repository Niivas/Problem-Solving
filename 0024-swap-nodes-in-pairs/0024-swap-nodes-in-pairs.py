# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return head

        # Initialize variables
        first, second = head, head.next
        ans = second
        prev = ListNode(0)

        # Swap pairs until the end or no pair left
        while first and second:
            # Preserve the reference to the next node
            temp = second.next

            # Connect the previous swapped pair to the new swapped pair
            prev.next = second

            # Swap the positions of the first and second nodes
            second.next = first

            # Connect the remaining nodes after the swapped pair
            first.next = temp

            # Update prev for the next iteration
            prev = first

            # Check if there are more nodes to swap
            if temp:
                first = first.next
                second = first.next
            else:
                break

        # Return the modified linked list's head
        return ans
