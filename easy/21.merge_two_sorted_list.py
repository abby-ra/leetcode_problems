class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to build the result list
        dummy = ListNode()
        current = dummy

        # Compare nodes from both lists one by one
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes (only one list can have leftover)
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return the head of the merged list
        return dummy.next
