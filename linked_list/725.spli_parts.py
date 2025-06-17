class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head, k):
        # Step 1: Count total nodes
        total_length = 0
        curr = head
        while curr:
            total_length += 1
            curr = curr.next

        # Step 2: Calculate base size and extra nodes
        part_size = total_length // k
        extra = total_length % k

        result = []
        curr = head

        # Step 3: Split into parts
        for i in range(k):
            part_head = curr
            size = part_size + (1 if i < extra else 0)

            for j in range(size - 1):
                if curr:
                    curr = curr.next

            if curr:
                temp = curr.next
                curr.next = None
                curr = temp

            result.append(part_head)

        return result
