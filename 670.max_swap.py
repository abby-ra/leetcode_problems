class Solution:
    def maximumSwap(self, num):
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}  # Map digit to last index

        for i, d in enumerate(digits):
            for bigger in range(9, int(d), -1):
                if last.get(bigger, -1) > i:
                    digits[i], digits[last[bigger]] = digits[last[bigger]], digits[i]
                    return int(''.join(digits))
        
        return num
