#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If one list is empty, return the other list
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Initialize a dummy head node
        head = ListNode(0)
        current = head

        # Traverse the list while there are values in both lists, if the value in list1 is lower than list2,
        # append lis1 to current and move list1
        # else, append lis2 to current and move list2
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            
            else:
                current.next = list2
                list2 = list2.next
            
            # Move current
            current = current.next
        
        # When there are remaining nodes in one list, test which list it is and returns their values
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list excluding the dummy head
        return head.next