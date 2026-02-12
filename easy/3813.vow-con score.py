class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = "aeiouAEIOU"
        vow,con = 0,0

        for i in s:
            if i in v:
                vow += 1
            elif i.isalpha():
                con += 1

        if con == 0:
            return 0
        return vow/con