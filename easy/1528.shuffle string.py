class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [''] * len(s)
        for i,char in enumerate(s):
            res[indices[i]] = char
        return ''.join(res)