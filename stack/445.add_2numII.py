class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []

        # Push all values from l1 and l2 to stacks
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while stack1 or stack2 or carry:
            total = carry
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()

            carry, digit = divmod(total, 10)

            # Create new node and link it
            node = ListNode(digit)
            node.next = head
            head = node

        return head
