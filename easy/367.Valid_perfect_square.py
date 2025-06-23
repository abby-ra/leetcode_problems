class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        r = int(num ** 0.5)
        return r * r == num
