class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        a = "".join(word1)
        b = "".join(word2)
        print(a)
        print(b)
        if a in b and len(a) == len(b):
            return True
        else:
            return False