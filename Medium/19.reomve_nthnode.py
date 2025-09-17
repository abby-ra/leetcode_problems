class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # First, find the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # If we need to remove the first node
        if n == length:
            return head.next

        # Find the node before the one we want to remove
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next

        # Remove the nth node from end
        curr.next = curr.next.next

        return head
