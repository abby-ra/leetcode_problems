class Solution:
    def makeFancyString(self, s):
        result = []
        for ch in s:
            if len(result) >= 2 and result[-1] == result[-2] == ch:
                continue  # Skip character to avoid three in a row
            result.append(ch)
        return ''.join(result)
