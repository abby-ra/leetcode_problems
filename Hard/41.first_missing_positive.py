class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)  # set lookup is O(1)
        i = 1
        while True:
            if i not in num_set:
                return i
            i += 1
