class Solution:
    def checkValidString(self, s):
        low = high = 0

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1    # treat '*' as ')'
                high += 1   # treat '*' as '('

            if high < 0:
                return False  # Too many ')'

            if low < 0:
                low = 0  # Can't have negative open brackets

        return low == 0
