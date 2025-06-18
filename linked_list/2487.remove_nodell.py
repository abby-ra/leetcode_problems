class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head):
        def reverse(node):
            prev = None
            while node:
                node.next, prev, node = prev, node, node.next
            return prev

        head = reverse(head)
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        max_val = curr.val
        prev = dummy

        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next

        return reverse(dummy.next)
