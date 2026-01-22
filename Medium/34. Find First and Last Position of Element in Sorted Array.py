class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        
        b = []

        for i in range(0,len(nums)):
            if nums[i] == target:
                b.append(i)

        if not b:
            return [-1,-1]
        return [b[0],b[-1]]
