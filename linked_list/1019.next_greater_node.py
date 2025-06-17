class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head):
        # Step 1: Convert linked list to an array
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # Step 2: Prepare result list and stack
        result = [0] * len(values)
        stack = []

        # Step 3: Traverse values and use stack to find next greater
        for i, val in enumerate(values):
            # While current value is greater than the value at index on top of stack
            while stack and val > values[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = val
            stack.append(i)

        return result
