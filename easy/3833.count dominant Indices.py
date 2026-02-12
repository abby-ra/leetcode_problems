class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        domin = 0
        for i in range(len(nums)-1):
            right = 0
            count = 0
            for j in range(i+1,len(nums)):
                right += nums[j]
                count += 1
            avg = right/count
            if nums[i] > avg:
                domin +=1
            
        return domin
        