class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = f = head

        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                break
        else:
            return None

        s = head
        while s != f:
            s = s.next
            f = f.next

        return s
