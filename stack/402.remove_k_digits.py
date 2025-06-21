class Solution:
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # Remove remaining digits from the end if needed
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"
