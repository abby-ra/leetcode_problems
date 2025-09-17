class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Convert binary strings to integers, add them, convert back to binary string
        result = bin(int(a, 2) + int(b, 2))
        return result[2:]  # remove the '0b' prefix
