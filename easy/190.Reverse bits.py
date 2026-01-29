class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # Take last bit and append to result
            result = (result << 1) | (n & 1)
            # Shift n to process next bit
            n >>= 1
        return result
