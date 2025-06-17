class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head, k):
        # Step 1: Count the total number of nodes
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Step 2: Find kth node from start and end
        first = head
        for _ in range(k - 1):
            first = first.next

        second = head
        for _ in range(length - k):
            second = second.next

        # Step 3: Swap their values
        first.val, second.val = second.val, first.val

        return head
