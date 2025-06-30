class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        result = ""
        while i < len(s):
            # Check if a two-digit mapping with '#' is possible
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i + 2])
                result += chr(ord('a') + num - 1)
                i += 3  # Skip the two digits and the '#'
            else:
                num = int(s[i])
                result += chr(ord('a') + num - 1)
                i += 1
        return result
