# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
