class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count =0

        for i in nums:
            c = len(str(i))
            if c%2 == 0:
                count += 1
        return count
