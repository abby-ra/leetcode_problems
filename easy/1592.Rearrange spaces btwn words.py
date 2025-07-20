class Solution:
    def reorderSpaces(self, t):
        s = t.count(' ')        # Total spaces
        w = t.split()           # List of words
        n = len(w)              # Number of words

        if n == 1:
            return w[0] + ' ' * s

        gap = s // (n - 1)      # Spaces between words
        extra = s % (n - 1)     # Extra spaces

        res = (' ' * gap).join(w)
        return res + ' ' * extra
