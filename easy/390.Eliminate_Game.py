class Solution:
    def lastRemaining(self, n):
        a = 1         # head
        b = 1         # step size
        left = True   # direction flag
        rem = n       # remaining elements

        while rem > 1:
            if left or rem % 2 == 1:
                a += b
            b *= 2
            rem //= 2
            left = not left

        return a
