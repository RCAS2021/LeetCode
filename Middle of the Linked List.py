# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = []
        current = head

        # Transforming linked list to normal list
        while current is not None:
            new_list.append(current.val)
            current = current.next

        middle = len(new_list) // 2

        # Transforming list to linked list
        # Setting first node
        head = ListNode(new_list[middle])
        current = head
        for item in new_list[middle+1:]:
            current.next = ListNode(item)
            current = current.next
            
        return head