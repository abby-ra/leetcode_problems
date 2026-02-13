class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = set(nums)
        mul = k
        while True:
            if mul not in s:
                return mul
            mul+=k

        