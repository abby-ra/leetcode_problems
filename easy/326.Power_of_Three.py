class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            while n%3 == 0:
                n//=3
            return n == 1
        else:
            return False
