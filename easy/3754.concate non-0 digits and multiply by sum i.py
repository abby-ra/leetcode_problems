class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        su = 0
        x = ""
        for i in s:
            if int(i)!=0:
                x+= i
                su += int(i)

        if x == "":
            return 0
        return int(x) * su
