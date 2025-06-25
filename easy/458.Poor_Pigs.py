class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        tests = minutesToTest // minutesToDie
        pigs = 0
        while (tests + 1) ** pigs < buckets:
            pigs += 1
        return pigs
        