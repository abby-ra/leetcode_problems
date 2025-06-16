class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # store next
            curr.next = prev       # reverse the link
            prev = curr            # move prev forward
            curr = next_node       # move curr forward

        return prev  # new head of the reversed list
