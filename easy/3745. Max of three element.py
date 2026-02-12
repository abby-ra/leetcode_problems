class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        nums.sort()
        
        smallest = nums[0]
        largest1 = nums[-1]
        largest2 = nums[-2]
        
        return largest1 + largest2 - smallest
