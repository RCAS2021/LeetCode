# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        # Creates two nodes, prev and curr who initially points to None and to the list head
        #prev, curr = None, head
        # Traverse through the list until curr is None
        #while curr is not None:
            # Store current next to next
        #    next = curr.next
            # Make current next to prev
        #    curr.next = prev
            # Make prev equal to current
        #    prev = curr
            # Make current equal to next
        #    curr = next
        #
        #return prev

        #recursively
        # If both are None, return head
        if head is None or head.next is None:
            return head

        # Create new node to call the function recursively
        res = self.reverseList(head.next)

        # Sets head node as head.next.next
        head.next.next = head
        # Changes head next to None
        head.next = None

        # Return the reversed list
        return res
