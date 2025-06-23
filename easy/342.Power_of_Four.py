class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            while n % 4 == 0:
                n//=4
            return n == 1
        else:
            return False
