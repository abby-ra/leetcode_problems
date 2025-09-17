class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Count total nodes
        count = 0
        node = head
        while node:
            count += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while count >= k:
            curr = prev.next
            nex = curr.next

            # Reverse k nodes
            for _ in range(1, k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next

            # Move prev to the end of the reversed group
            prev = curr
            count -= k

        return dummy.next
