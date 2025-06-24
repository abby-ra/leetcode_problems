class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_digits = "0123456789abcdef"
        res = ""
        
        # Convert negative to 32-bit unsigned
        num &= 0xFFFFFFFF

        while num:
            res = hex_digits[num % 16] + res
            num //= 16

        return res
