class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        small = sum(nums[:k])
        lar = sum(nums[-k:])

        return abs(lar - small)
        