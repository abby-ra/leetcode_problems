class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = []

        for i in range(min(nums),max(nums)):
            if i not in nums:
                num.append(i)
        if len(num)>0:
            return num
        return list()