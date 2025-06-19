class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            # Replace n with the sum of squares of its digits
            n = sum(int(digit) ** 2 for digit in str(n))

        return True
