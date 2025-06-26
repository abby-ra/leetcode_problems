class Solution:
    def countDigitOne(self, n):
        r, d = 0, 1
        while d <= n:
            a, b, c = n // (d*10), (n//d)%10, n%d
            r += a*d if b == 0 else a*d + c + 1 if b == 1 else (a+1)*d
            d *= 10
        return r
