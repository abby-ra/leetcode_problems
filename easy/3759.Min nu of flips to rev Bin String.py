class Solution(object):
    def minimumFlips(self, n):
        s = bin(n)[2:]
        rev= s[::-1]
        flip = 0

        for i in range(len(s)):
            if s[i] != rev[i]:
                flip+=1

        return flip
