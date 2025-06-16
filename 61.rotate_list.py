class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list and the last node
        length = 1
        last_node = head
        while last_node.next:
            last_node = last_node.next
            length += 1

        # Step 2: Make the list circular
        last_node.next = head

        # Step 3: Calculate how many steps to the new tail
        k = k % length
        steps_to_tail = length - k
        new_tail = head
        for _ in range(steps_to_tail - 1):
            new_tail = new_tail.next

        # Step 4: Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
