class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        p = 1
        for i in str(n):
            s += int(i)
            p *= int(i)
        return p - s