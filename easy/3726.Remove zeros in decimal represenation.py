class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        st = str(n)
        s = ""
        for i in st:
            if i != '0':
                s+=i

        return int(s)