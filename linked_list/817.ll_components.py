# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        n_set = set(nums)
        count = 0
        cur = head

        while cur:
            if cur.val in n_set and (cur.next is None or cur.next.val not in n_set):
                count+=1
            cur =cur.next

        return count