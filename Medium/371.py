class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # to handle 32-bit overflow

        while b != 0:
            temp = (a ^ b) & mask   # sum without carry
            b = ((a & b) << 1) & mask  # carry
            a = temp

        # handle negative numbers
        if a <= 0x7FFFFFFF:
            return a
        else:
            return ~(a ^ mask)
