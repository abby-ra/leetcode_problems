class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)[::-1]  # Reverse the number string
        parts = [s[i:i+3] for i in range(0, len(s), 3)]  # Split into groups of 3
        return '.'.join(parts)[::-1]  # Join with dot and reverse back
