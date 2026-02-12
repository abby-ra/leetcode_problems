class Solution(object):
    def largestEven(self, s):
        # Traverse from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '2':
                return s[:i + 1]
        
        # If no '2' found
        return ""
