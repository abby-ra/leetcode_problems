# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums_set = set(nums)  # ✅ Faster lookups

        dummy = ListNode(0)
        tail = dummy
        cur = head

        while cur:
            if cur.val not in nums_set:
                tail.next = ListNode(cur.val)
                tail = tail.next
            cur = cur.next

        return dummy.next
