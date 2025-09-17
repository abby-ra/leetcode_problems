class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        m = str(x)
        n = m[::-1]
        if m == n:
            return True
        return False
