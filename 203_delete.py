class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # while head:
        #     if head.val==val:
        #         head=head.next
        dummy = ListNode(0)
        dummy.next=head
        head = dummy    
        top = head
        while top and top.next:
            if top.next.val==val:
                top.next=top.next.next
            else:
                top=top.next
        return head.nextz