class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        a = pattern
        b = s.split()

        if len(a) != len(b):
            return False

        d1 = {}
        d2 = {}

        for i in range(len(a)):
            if a[i] in d1:
                if d1[a[i]] != b[i]:
                    return False
            else:
                if b[i] in d2:
                    return False
                d1[a[i]] = b[i]
                d2[b[i]] = a[i]
        return True