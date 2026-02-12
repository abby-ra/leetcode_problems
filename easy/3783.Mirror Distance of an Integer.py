class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        if int(str(n)) >= 10:
            return abs(n - int(str(n)[::-1]))
        else:
            return 0