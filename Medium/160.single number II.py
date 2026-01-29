class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                a.append(nums[i])
        return a