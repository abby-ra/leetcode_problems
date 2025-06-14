class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Convert list of digits to string, then to int
        n = int("".join(map(str, digits))) + 1
        # Convert the result back to list of digits
        return list(map(int, str(n)))
 